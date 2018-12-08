# -----------------------------------------------------------------------------
# flatteparser.py
#
# An interpreter for Flatte(2), built by modifying the simple calculator 
# example from http://www.dabeaz.com/ply/example.html
# but one that builds AST and then evaluates it.
#
# C. R. Ramakrishnan, 2018.
#
# This is the parser.
#
# -----------------------------------------------------------------------------

import ply.yacc as yacc
import flattelexer
from flattelexer import tokens, lex
import flatteerror
import flatteast

# Parsing rules

precedence = (
    ('nonassoc', 'LET', 'IN'),
    ('nonassoc', 'IF', 'ELSE'),
    ('right', 'OR'),
    ('right', 'AND'), 
    ('left','EQUALS','NOTEQUALS', 'LEQ', 'GEQ', 'LT', 'GT'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE', 'MOD'),
    ('nonassoc', 'FUN', 'ARROW'),
    ('nonassoc','NOT', 'FST', 'SND'),
    ('right', 'APPLY'),
    )


def p_statements_empty(t):
    'statements : empty'
    t[0] = []
    
def p_statements_multiple(t):
    'statements : statement DOUBLESEMICOLON statements'
    t[0] = t[1] + t[3]

    
def p_statement_expression(t):
    'statement : expression'
    t[0] = [t[1]]
def p_statement_command(t):
    'statement : command'
    t[0] = t[1]
    
    
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression EQUALS expression
                  | expression LEQ expression
                  | expression LT expression
                  | expression GEQ expression
                  | expression GT expression
                  | expression AND expression
                  | expression OR expression
                  | expression NOTEQUALS expression'''
    t[0] = flatteast.BinaryExpr(t[2], t[1], t[3], t.lineno(2))
    
def p_expression_unary(t):
    '''expression : MINUS expression %prec NOT
                  | FST expression
                  | SND expression
                  | NOT expression'''
    t[0] = flatteast.UnaryExpr(t[1], t[2], t.lineno(1))

def p_expression_let(t):
    'expression : LET NAME EQUALS expression IN expression'
    t[0] = flatteast.LetExpr(t[2], t[4], t[6], t.lineno(1))

def p_expression_let_fundef(t):
    'expression : LET NAME args EQUALS expression IN expression'
    t[0] = flatteast.LetExpr(t[2], fundef(t[3], t[5], t.lineno(2)), t[7], t.lineno(1))

def p_expression_if(t):
    'expression : IF expression THEN expression ELSE expression'
    t[0] = flatteast.IfExpr(t[2], t[4], t[6], t.lineno(1))

def p_expression_apply(t):
    'expression : basicexpression basicexpression %prec APPLY'
    t[0] = flatteast.ApplyExpr(t[1], t[2], t.lineno(1))

def p_expression_fundef(t):
    'expression : FUN NAME ARROW expression'
    t[0] = flatteast.FunDefExpr(t[2], t[4], t.lineno(1))

def p_expression_basic(t):
    'expression : basicexpression'
    t[0] = t[1]


def p_basicexpression_group(t):
    'basicexpression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_basicexpression_pair(t):
    'basicexpression : LPAREN expression COMMA expression RPAREN'
    t[0] = flatteast.PairExpr(t[2], t[4], t.lineno(1))

def p_basicexpression_true(t):
    'basicexpression : TRUE'
    t[0] = flatteast.BoolConstExpr(True, t.lineno(1))

def p_basicexpression_false(t):
    'basicexpression : FALSE'
    t[0] = flatteast.BoolConstExpr(False, t.lineno(1))

def p_basicexpression_number(t):
    'basicexpression : NUMBER'
    t[0] = flatteast.IntConstantExpr(t[1], t.lineno(1))

def p_basicexpression_name(t):
    'basicexpression : NAME'
    t[0] = flatteast.NameExpr(t[1], t.lineno(1))


def p_args_single(t):
    'args : arg'
    t[0] = [t[1]]

def p_args_multiple(t):
    'args : arg args'
    t[0] = [t[1]] + t[2]

def p_arg_name(t):
    'arg : NAME'
    t[0] = [t[1]]

def p_arg_pair(t):
    'arg : LPAREN NAME COMMA NAME RPAREN'
    t[0] = [t[2], t[4]]


def p_command(t):
    'command : CMD_USE SIMPLESTRING'
    filename = t[2]
    f = open(filename, 'r')   # leave any execeptions to be seen from outside
    s = f.read()
    newlexer = lex.lex(flattelexer)
    newparser = yacc.yacc()
    t[0] = newparser.parse(s, lexer=newlexer, debug=None)
    

def p_empty(t):
    'empty :'
    pass

def p_error(t):
    if (t == None):
        raise flatteerror.ParserError('Expression does not end with ";;"')
    else:
        raise flatteerror.ParserError("near symbol '{0}' in line {1}".format(t.value, t.lineno))

def fundef(args, expr, lineno):
    if len(args) == 1:
        return make_fundef_from_arg(args[0], expr, lineno)
    else:
        fd = fundef(args[1:], expr, lineno)
        return make_fundef_from_arg(args[0], fd, lineno)

def make_fundef_from_arg(args, expr, lineno):
    if len(args) == 1:
        # single argument:
        return flatteast.FunDefExpr(args[0], expr, lineno)
    else:
        # pair, so args = [a1, a2]
        fst = args[0]
        snd = args[1]
        innermost = flatteast.LetExpr(snd, flatteast.UnaryExpr("snd", flatteast.NameExpr("__arg", lineno), lineno), expr, lineno)
        nextouter = flatteast.LetExpr(fst, flatteast.UnaryExpr("fst", flatteast.NameExpr("__arg", lineno), lineno), innermost, lineno)
        return flatteast.FunDefExpr("__arg", nextouter, lineno)
    
    
parser = yacc.yacc()
