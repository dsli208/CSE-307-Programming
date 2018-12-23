# -----------------------------------------------------------------------------
# calclexer.py
#
# A simple calculator with variables.
# The example from http://www.dabeaz.com/ply/example.html
# broken down into separate lexer, parser, and main (top-level) files 
#
# This is the lexer
#
# -----------------------------------------------------------------------------

import ply.lex as lex

# Tokens
tokens = (
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN',
    )

# Patterns
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)   # will not raise Value error due to the \d+ RE pattern
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s', skipped" % t.value[0])
    t.lexer.skip(1)
    
