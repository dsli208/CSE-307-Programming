# -----------------------------------------------------------------------------
# calcast.py
#
# A more elaborate version of the same calculator as the one in
# http://www.dabeaz.com/ply/example.html
# This version first builds the AST and then evaluates it.
#
# This is the AST definition for that version
#
# -----------------------------------------------------------------------------

from calcerror import InternalError, EvalError

names = {}  # dictionary of all names seen so far

class Expr(object):
    ''' Dummy class representing all expressions'''
    def __str__(self):
        return "Unknown expression"
    def printout(self):
        print self, 


class IntConstantExpr(Expr):
    ''' Instances of this class represent integer constants'''
    def __init__(self, arg, lineno):
        self.lineno = lineno   # Line number in the source program
        self.value = arg         # The integer constant (an int)
            
    def __str__(self):
        return "Integer(%d)"%self.value

    def eval(self):
        return self.value


class NameExpr(Expr):
    ''' Instances of this class represent names'''
    def __init__(self, name, lineno):
        self.lineno = lineno   # Line number in the source program
        self.name = name       # The name itself (a string)
    def __str__(self):
        return "Name(%d)"%self.name

    def eval(self):
        global names  # dictionary of all known names and their values
        try:
            return names[self.name]
        except LookupError:
            raise EvalError("Undefined name %s in lineno %d" % (self.name, self.lineno))
    

class UnaryExpr(Expr):
    ''' Instances of this class represent unary expressions'''
    operators = ["-"]   # only one unary operator for now
    def __init__(self, uop, expr, lineno):
        if (uop not in UnaryExpr.operators):
            raise InternalError("Unknown unary operator: %s in lineno %d"% (uop, lineno))            
        self.lineno = lineno   # Line number in the source program
        self.uop = uop         # The unary operator, one of operators
        self.arg = expr        # The argument, which is another Expr
        
    def __str__(self):
        return "Unary({0}, {1})".format(self.uop, self.arg)

    def eval(self):
        arg_value = self.arg.eval()
        if (self.uop == "-"):
            return - arg_value
        else:
            raise InternalError("Unknown unary operator: %s in lineno %d"% (self.uop, self.lineno))
        
        
class BinaryExpr(Expr):
    ''' Instances of this class represent binary expressions'''
    operators = ["+", "-", "*", "/"]
    def __init__(self, bop, arg1, arg2, lineno):
        if (bop not in BinaryExpr.operators):
            raise InternalError("Unknown binary operator: %s in lineno %d"% (bop, lineno))            
        self.lineno = lineno   # Line number in the source program
        self.bop = bop         # The binary operator, one of operators
        self.arg1 = arg1       # The first argument, which is another Expr
        self.arg2 = arg2       # The second argument, which is another Expr
    def __str__(self):
        return "Binary({0}, {1}, {2})".format(self.bop,self.arg1,self.arg2)

    def eval(self):
        arg1_value = self.arg1.eval()
        arg2_value = self.arg2.eval()
        if (self.bop == "+"):
            return arg1_value + arg2_value
        if (self.bop == "-"):
            return arg1_value - arg2_value
        if (self.bop == "*"):
            return arg1_value * arg2_value
        if (self.bop == "/"):
            return arg1_value / arg2_value
        else:
            raise InternalError("Unknown binary operator: %s in lineno %d"% (self.bop, self.lineno))

class Stmt(object):
    '''Dummy class representing all statements (commands)'''
    def __str__(self):
        return "Unknown statement"
    def printout(self):
        print self, 

class AssignStmt(Stmt):
    ''' Instances of this class represent assignment statement'''
    def __init__(self, name, expr, lineno):
        self.lineno = lineno   # Line number in the source program
        self.name = name       # Left-hand side variable (string)
        self.expr = expr       # Right-hand side expression
    def __str__(self):
        return "Assign({0}, {1})".format(self.name, self.expr)
        
    def eval(self):
        global names
        rhs_value = self.expr.eval()
        names[self.name] = rhs_value

class ExprStmt(Stmt):
    ''' Instances of this class represent expression statements, i.e. commands that are themselves expressions'''
    def __init__(self, expr, lineno):
        self.lineno = lineno   # Line number in the source program
        self.expr = expr       # The expression
    def __str__(self):
        return "Expr({0})".format(self.expr)

    def eval(self):
        return self.expr.eval()
