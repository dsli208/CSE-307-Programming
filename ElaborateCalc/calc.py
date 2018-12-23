# -----------------------------------------------------------------------------
# calc.py
#
# A more elaborate version of the same calculator as the one in
# http://www.dabeaz.com/ply/example.html
# This version first builds the AST and then evaluates it.
#
# This is the top-level of that version
#
# -----------------------------------------------------------------------------

from calcparser import parser
import calclexer
from calclexer import lex
from calcerror import CalcError

while True:
    try:
        s = raw_input('calc > ')   # Use raw_input on Python 2
        ast = parser.parse(s, lexer=lex.lex(calclexer), debug=None)
        print ast.eval()
    except EOFError:
        print ''  # print a new-line and quit
        break
    except CalcError as e:   # if there is any error
        print e  # print the error and continue
