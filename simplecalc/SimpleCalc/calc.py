# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.
# The example from http://www.dabeaz.com/ply/example.html
# broken down into separate lexer, parser, and main (top-level) files 
#
# This is the top-level
#
# -----------------------------------------------------------------------------

from calcparser import parser
import calclexer
from calclexer import lex

while True:
    try:
        s = raw_input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s, lexer=lex.lex(calclexer), debug=None)

