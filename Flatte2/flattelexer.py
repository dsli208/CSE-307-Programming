# -----------------------------------------------------------------------------
# flattelexer.py
#
# An interpreter for Flatte(2), built by modifying the simple calculator 
# example from http://www.dabeaz.com/ply/example.html
# but one that builds AST and then evaluates it.
#
# C. R. Ramakrishnan, 2018.
#
# This is the lexer
#
# -----------------------------------------------------------------------------

import ply.lex as lex


# Reserved words
reserved = {
    'mod': 'MOD',
    'not': 'NOT',
    'true': 'TRUE',
    'false': 'FALSE',
    'let': 'LET',
    'in': 'IN',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'fun': 'FUN',
    'fst': 'FST',
    'snd': 'SND',
    }

# Tokens
tokens = [
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE', 
    'EQUALS',
    'NOTEQUALS', 'LEQ', 'GEQ', 'LT', 'GT',
    'AND', 'OR',
    'LPAREN','RPAREN',
    'ARROW',
    'COMMA',
    'DOUBLESEMICOLON',
    'SIMPLESTRING',
    'CMD_USE',
    ] + list(reserved.values())

# Patterns
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_NOTEQUALS  = r'<>'
t_LEQ = r'<='
t_GEQ = r'>='
t_LT = r'<'
t_GT = r'>'
t_AND = r'&&'
t_OR = r'\|\|'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ARROW = r'->'
t_COMMA = r','
t_DOUBLESEMICOLON = r';;'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)   # will not raise Value error due to the \d+ RE pattern
    return t

def t_SIMPLESTRING(t):
    r'"[^"]*"'
    t.value = t.value[1:(len(t.value)-1)]
    return t

def t_CMD_USE(t):
    r'\#use'
    return t

def t_COMMENT(t):
    r'\(\* ([^\)\*] | \*[^\)])* \*\)'
    pass

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s', skipped" % t.value[0])
    t.lexer.skip(1)
    
