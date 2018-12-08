# -----------------------------------------------------------------------------
# flatte.py
#
# An interpreter for Flatte(1), built by modifying the simple calculator 
# example from http://www.dabeaz.com/ply/example.html
# but one that builds AST and then evaluates it.
#
# C. R. Ramakrishnan, 2018.
#
# This is the top-level
#
# -----------------------------------------------------------------------------

""" Flatte Interpreter
An interpreter for Flatte programs
Usage: python iflatte.py 
This will give a series of prompts, 'iflatte > ' and interpret the input as
Flatte expressions.  Use end of file character to terminate the interpreter.
"""
import sys
import getopt

from flatteparser import parser
import flattelexer
from flattelexer import lex
from flatteerror import FlatteError

            
while True:
    try:
        if (sys.version_info > (3,0)):
            s = input('iflatte > ')   # Use input on Python 3
        else:
            s = raw_input('iflatte > ')   # Use raw_input on Python 2.x
            
        ast = parser.parse(s, lexer=lex.lex(flattelexer), debug=None)
        for e in ast:
            # FOR DEBUGGING, uncomment the following line, so you can see the parsed expression
            #        print e
            print (e.eval({})) # with the empty environment
    except EOFError:
        print ('')  # print a new-line and quit
        break
    except FlatteError as e:   # if there is any error
        print (e)  # print the error and continue
