# -----------------------------------------------------------------------------
# flatteast.py
#
# An interpreter for Flatte(1), built by modifying the simple calculator
# example from http://www.dabeaz.com/ply/example.html
# but one that builds AST and then evaluates it.
#
# C. R. Ramakrishnan, 2018.
#
# This file has the definitions of classes that form the AST.
# The interpreter is implemented by method "eval" in each class.
#
# -----------------------------------------------------------------------------
from flatteerror import InternalError, EvalError

# Exception to mark unimplemented evaluation functions
class Unimplemented(Exception):
    pass



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
        self.value = arg       # The integer constant (an int)

    def __str__(self):
        return "Integer({0})".format(self.value)

    def eval(self, env):
        return self.value


class BoolConstExpr(Expr):
    ''' Instances of this class represent boolean constant (true/false)'''
    def __init__(self, arg, lineno):
        self.lineno = lineno   # Line number in the source program
        self.value = arg       # The boolean constant (a boolean value)

    def __str__(self):
        return "Boolean({0})".format(self.value)

    def eval(self, env):
        return self.value


class NameExpr(Expr):
    ''' Instances of this class represent names'''
    def __init__(self, name, lineno):
        self.lineno = lineno   # Line number in the source program
        self.name = name       # The name itself (a string)
    def __str__(self):
        return "Name(%d)"%self.name

    def eval(self, env):
        try:
            return env[self.name]
        except LookupError:
            raise EvalError("Undefined name %s in lineno %d" % (self.name, self.lineno))


class UnaryExpr(Expr):
    ''' Instances of this class represent unary expressions'''
    operators = ["-", "not"]
    def __init__(self, uop, expr, lineno):
        if (uop not in UnaryExpr.operators):
            raise InternalError("Unknown unary operator: %s in lineno %d"% (uop, lineno))
        self.lineno = lineno   # Line number in the source program
        self.uop = uop         # The unary operator, one of operators
        self.arg = expr        # The argument, which is another Expr

    def __str__(self):
        return "Unary({0}, {1})".format(self.uop, self.arg)

    def eval(self, env):
        arg_value = self.arg.eval(env)
        if (self.uop == "-"):
            return - arg_value
        elif (self.uop == "not"):
            # What is self.op?  Doesn't look defined.
            return not arg_value
            # Implement the "not"
            #raise Unimplemented("Unimplemented evaluation for unary operator %s at line %d"% (self.uop, self.lineno))
        else:
            raise InternalError("Unknown unary operator: %s in lineno %d"% (self.uop, self.lineno))


class BinaryExpr(Expr):
    ''' Instances of this class represent binary expressions'''
    operators = ["+", "-", "*", "/", "mod",
                 "=", "<>", "<=", ">=", "<", ">",
                 "&&", "||"]
    def __init__(self, bop, arg1, arg2, lineno):
        if (bop not in BinaryExpr.operators):
            raise InternalError("Unknown binary operator: %s in lineno %d"% (bop, lineno))
        self.lineno = lineno   # Line number in the source program
        self.bop = bop         # The binary operator, one of operators
        self.arg1 = arg1       # The first argument, which is another Expr
        self.arg2 = arg2       # The second argument, which is another Expr
    def __str__(self):
        return "Binary({0}, {1}, {2})".format(self.bop,self.arg1,self.arg2)

    def eval(self, env):
        arg1_value = self.arg1.eval(env)
        arg2_value = self.arg2.eval(env)
        if (self.bop == "+"):
            return arg1_value + arg2_value
        elif (self.bop == "-"):
            return arg1_value - arg2_value
        elif (self.bop == "*"):
            return arg1_value * arg2_value
        elif (self.bop == "/"):
            return arg1_value / arg2_value
        elif (self.bop == "mod"):
            return arg1_value % arg2_value
            # Can't we just evaluate each of the other expressions?
            #raise Unimplemented("Unimplemented evaluation for binary operator: %s in lineno %d"% (self.bop, self.lineno))
            # IMPLEMENTATION OF LEFT OUT OPERATORS IS BELOW.  note some of them use different symbols to make it compatible with Python
        elif (self.bop == "="):
            if (arg1_value == arg2_value):
                return True
            else:
                return False
        elif (self.bop == "<>"):
            if (arg1_value == arg2_value):
                return False
            else:
                return True
        elif (self.bop == "<="):
            if (arg1_value <= arg2_value):
                return True
            else:
                return False
        elif (self.bop == ">="):
            if (arg1_value >= arg2_value):
                return True
            else:
                return False
        elif (self.bop == ">"):
            if (arg1_value > arg2_value):
                return True
            else:
                return False
        elif (self.bop == "<"):
            if (arg1_value < arg2_value):
                return True
            else:
                return False
        elif (self.bop == "||"):
            if (arg1_value > 0 or arg2_value > 0):
                return True
            else:
                return False
        elif (self.bop == "&&"):
            if (arg1_value > 0 and arg2_value > 0):
                return True
            else:
                return False
        else:
            raise InternalError("Unknown binary operator: %s in lineno %d"% (self.bop, self.lineno))


class IfExpr(Expr):
    ''' Instances of this class represent conditional (if) expressions'''
    def __init__(self, cond, thenpart, elsepart, lineno):
        self.lineno = lineno   # Line number in the source program
        self.cond = cond       # Condition part of the "if"  (e.g. c in   "if c then e1 else e2")
        self.thenpart = thenpart  # Then part of "if"  (e.g. e1 in   "if c then e1 else e2")
        self.elsepart = elsepart  # Else part of "if"  (e.g. e2 in   "if c then e1 else e2")

    def __str__(self):
        return "If({0}, {1}, {2})".format(self.cond, self.thenpart, self.elsepart)

    # Test this
    # Complete eval function for if.  Then part is returned if cond_value, else return elsepart
    def eval(self, env):
        cond_value = self.cond.eval(env)
        if (cond_value == True):
            return self.thenpart.eval(env)
        else:
            return self.elsepart.eval(env)


# STUDY LET EXPRESSIONS MORE
class LetExpr(Expr):
    ''' Instances of this class represent let expressions'''
    def __init__(self, name, defexpr, useexpr, lineno):
        self.lineno = lineno   # Line number in the source program
        self.name = name       # Name defined by "let"  (e.g. x   in  "let x = e1 in e2")
        self.defexpr = defexpr # Value of that name  (e.g. e1   in  "let x = e1 in e2")
        self.useexpr = useexpr # Expression where that name is used (e.g. e2   in  "let x = e1 in e2")

    def __str__(self):
        return "Let({0}, {1}, {2})".format(self.name, self.defexpr, self.useexpr)

        # Eval: First two lines are setting x (def_expr_value) to the associated value (env[self.name])
        # Once that is done, call the portion that goes after "in"
    def eval(self, env):
        def_expr_value = self.defexpr.eval(env)
        env[self.name] = def_expr_value
        return self.useexpr.eval(env)
