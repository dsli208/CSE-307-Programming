# -----------------------------------------------------------------------------
# flatterrorlrd.py
#
# An interpreter for Flatte(2), built by modifying the simple calculator 
# example from http://www.dabeaz.com/ply/example.html
# but one that builds AST and then evaluates it.
#
# C. R. Ramakrishnan, 2018.
#
# This file has the exception definitions
#
# -----------------------------------------------------------------------------
class FlatteError(Exception):
    '''All errors from the calculator are instances of this class'''
    pass

class ParserError(FlatteError):
    '''Parser error: means there was a syntax error in the input'''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Syntax Error: %s" % self.value
    
class InternalError(FlatteError):
    '''Internal error: means there was something inconsistent in the definition of the calculuator'''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Internal Error: %s" % self.value
    
class EvalError(FlatteError):
    '''Internal error: means there was something inconsistent in the definition of the calculuator'''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Evaluation Error: %s" % self.value

