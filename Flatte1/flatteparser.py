# -----------------------------------------------------------------------------
# flatteparser.py
#
# An interpreter for Flatte(1), built by modifying the simple calculator 
# example from http://www.dabeaz.com/ply/example.html
# but one that builds AST and then evaluates it.
#
# C. R. Ramakrishnan, 2018.
#
# This is the parser.
#
# -----------------------------------------------------------------------------

import ply.yacc as yacc
from flattelexer import tokens
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
    ('nonassoc','NOT'),
    )


def p_toplevel(t):
    'statement : expression'
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
                  | NOT expression'''
    t[0] = flatteast.UnaryExpr(t[1], t[2], t.lineno(1))

def p_expression_let(t):
    'expression : LET NAME EQUALS expression IN expression'
    t[0] = flatteast.LetExpr(t[2], t[4], t[6], t.lineno(1))

def p_expression_if(t):
    'expression : IF expression THEN expression ELSE expression'
    t[0] = flatteast.IfExpr(t[2], t[4], t[6], t.lineno(1))

def p_expression_basic(t):
    'expression : basicexpression'
    t[0] = t[1]


def p_basicexpression_group(t):
    'basicexpression : LPAREN expression RPAREN'
    t[0] = t[2]

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

def p_error(t):
    raise flatteerror.ParserError("near symbol '%s' in line %d" % (t.value, t.lineno(1)))

parser = yacc.yacc()
