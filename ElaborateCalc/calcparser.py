# -----------------------------------------------------------------------------
# calcparser.py
#
# A more elaborate version of the same calculator as the one in
# http://www.dabeaz.com/ply/example.html
# This version first builds the AST and then evaluates it.
#
# This is the parser for that version
#
# -----------------------------------------------------------------------------

import ply.yacc as yacc
from calclexer import tokens
import calcerror
import calcast

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('nonassoc','UMINUS'),
    )


def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    t[0] = calcast.AssignStmt(t[1], t[3], t.lineno(1))
    
def p_statement_expr(t):
    'statement : expression'
    t[0] = calcast.ExprStmt(t[1], t.lineno(1))

    
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    t[0] = calcast.BinaryExpr(t[2], t[1], t[3], t.lineno(2))
    
def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = calcast.UnaryExpr(t[1], t[2], t.lineno(1))

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = calcast.IntConstantExpr(t[1], t.lineno(1))

def p_expression_name(t):
    'expression : NAME'
    t[0] = calcast.NameExpr(t[1], t.lineno(1))

def p_error(t):
    raise calcerror.ParserError("at  '%s'" % t.value)

parser = yacc.yacc()
