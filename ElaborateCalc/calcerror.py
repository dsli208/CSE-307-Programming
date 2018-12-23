# -----------------------------------------------------------------------------
# calcerror.py
#
# A more elaborate version of the same calculator as the one in
# http://www.dabeaz.com/ply/example.html
# This version first builds the AST and then evaluates it.
#
# This file has the exception definitions for that version
#
# -----------------------------------------------------------------------------

class CalcError(Exception):
    '''All errors from the calculator are instances of this class'''
    pass

class ParserError(CalcError):
    '''Parser error: means there was a syntax error in the input'''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Syntax Error: %s" % self.value
    
class InternalError(CalcError):
    '''Internal error: means there was something inconsistent in the definition of the calculuator'''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Internal Error: %s" % self.value
    
class EvalError(CalcError):
    '''Internal error: means there was something inconsistent in the definition of the calculuator'''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Evaluation Error: %s" % self.value

