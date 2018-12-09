# -----------------------------------------------------------------------------
# flatteast.py
#
# An interpreter for Flatte(2), built by modifying the simple calculator
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
import copy

class Expr(object):
    ''' Dummy class representing all expressions'''
    def __str__(self):
        return "Unknown expression"


class IntConstantExpr(Expr):
    ''' Instances of this class represent integer constants'''
    def __init__(self, arg, lineno):
        self.lineno = lineno
        self.value = arg

    def __str__(self):
        return "Integer({0})".format(self.value)

    def eval(self, env):
        return self.value


class BoolConstExpr(Expr):
    ''' Instances of this class represent boolean constant (true/false)'''
    def __init__(self, arg, lineno):
        self.lineno = lineno
        self.value = arg

    def __str__(self):
        return "Boolean({0})".format(self.value)

    def eval(self, env):
        return self.value


class NameExpr(Expr):
    ''' Instances of this class represent names'''
    def __init__(self, name, lineno):
        self.lineno = lineno
        self.name = name
    def __str__(self):
        return "Name({0})".format(self.name)

    def eval(self, env):
        try:
            return env[self.name]
        except LookupError:
            raise EvalError("Undefined name %s in lineno %d" % (self.name, self.lineno))


class UnaryExpr(Expr):
    ''' Instances of this class represent unary expressions'''
    operators = ["-", "not", "fst", "snd"]
    def __init__(self, uop, expr, lineno):
        if (uop not in UnaryExpr.operators):
            raise InternalError("Unknown unary operator: %s in lineno %d"% (uop, lineno))
        self.lineno = lineno
        self.uop = uop
        self.arg = expr

    def __str__(self):
        return "Unary({0}, {1})".format(self.uop, self.arg)

    def eval(self, env):
        arg_value = self.arg.eval(env)
        if (self.uop == "-"):
            return - arg_value
        elif (self.uop == "not"):
            return not arg_value
        elif (self.uop == "fst"):
            return arg_value.arg1
        elif (self.uop == "snd"):
            return arg_value.arg2
        elif (self.uop in UnaryExpr.operators):
            raise Unimplemented("Unimplemented evaluation for unary operator %s at line %d"% (self.uop, self.lineno))
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
        self.lineno = lineno
        self.bop = bop
        self.arg1 = arg1
        self.arg2 = arg2
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
        elif (self.bop == "="):
            return arg1_value == arg2_value
        elif (self.bop == "<>"):
            return arg1_value != arg2_value
        elif (self.bop == "<="):
            return arg1_value <= arg2_value
        elif (self.bop == "<"):
            return arg1_value < arg2_value
        elif (self.bop == ">="):
            return arg1_value >= arg2_value
        elif (self.bop == ">"):
            return arg1_value > arg2_value
        elif (self.bop == "||"):
            return arg1_value or arg2_value
        elif (self.bop == "&&"):
            return arg1_value and arg2_value
        elif (self.bop in BinaryExpr.operators):
            raise Unimplemented("Unimplemented evaluation for binary operator: %s in lineno %d"% (self.bop, self.lineno))
        else:
            raise InternalError("Unknown binary operator: %s in lineno %d"% (self.bop, self.lineno))


class IfExpr(Expr):
    ''' Instances of this class represent conditional (if) expressions'''
    def __init__(self, cond, thenpart, elsepart, lineno):
        self.lineno = lineno
        self.cond = cond
        self.thenpart = thenpart
        self.elsepart = elsepart

    def __str__(self):
        return "If({0}, {1}, {2})".format(self.cond, self.thenpart, self.elsepart)


    def eval(self, env):
        if (self.cond.eval(env)):
            return self.thenpart.eval(env)
        else:
            return self.elsepart.eval(env)


class LetExpr(Expr):
    ''' Instances of this class represent let expressions'''
    def __init__(self, name, defexpr, useexpr, lineno):
        self.lineno = lineno
        self.name = name
        self.defexpr = defexpr
        self.useexpr = useexpr

    def __str__(self):
        return "Let({0}, {1}, {2})".format(self.name, self.defexpr, self.useexpr)


    def eval(self, env):
        defval = self.defexpr.eval(env)
        newenv = copy.copy(env)
        newenv[self.name] = defval
        return self.useexpr.eval(newenv)

class PairExpr(Expr):
    ''' Instances of this class represent pair construction expressions'''
    def __init__(self, arg1, arg2, lineno):
        self.lineno = lineno
        self.arg1 = arg1
        self.arg2 = arg2
    def __str__(self):
        return "Pair({0}, {1})".format(self.arg1,self.arg2)

    def eval(self, env):
        arg1_val = self.arg1.eval(env)
        arg2_val = self.arg2.eval(env)
        return PairExpr(arg1_val, arg2_val, self.lineno)


class ApplyExpr(Expr):
    ''' Instances of this class represent apply (call) expressions'''
    def __init__(self, funexpr, argexpr, lineno):
        self.lineno = lineno   # Line number in the source program
        self.funexpr = funexpr # Expression that stands for the function being invoked
        self.argexpr = argexpr # Expression that stands for the corresponding argument

    def __str__(self):
        return "Apply({0}, {1})".format(self.funexpr, self.argexpr)


    def eval(self, env):

        funval = self.funexpr.eval(env)
        argval = self.argexpr.eval(env)
        #print("ApplyExpr")
        #print(funval, "-", argval, "-", env)
        funval[funval["param"]] = argval
        # Get the old env first
        return funval["body"].eval(funval)


class FunDefExpr(Expr):
    ''' Instances of this class represent function definition (lambda) expressions'''
    def __init__(self, param, body, lineno):
        self.lineno = lineno   # Line number in the source program
        self.param = param # Name of the formal parameter (x in x -> e)
        self.body = body # Expression in the body of the defined function (e in x -> e)
        #self.env = None

    def __str__(self):
        return "Fun({0}, {1})".format(self.param, self.body)

    def eval(self, env):
        #print("FunDefExpr")
        #print(self.body, "-", self.param, "-", env)
        #env[self.param] = self.body
        #self.env = env
        newenv = copy.copy(env)
        newenv["body"] = self.body
        newenv["param"] = self.param
        return newenv
