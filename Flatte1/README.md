# CSE 307: Principles of Programming Languages - Fall 2018
## Homework #2
## Due: Tue., Oct 23
In this assignment, you will fill parts of an interpreter for Flatte, an OCaml-like functional programming language. For this homework, we will start with a (simple) calculator, implemented using Python and the PLY parser framework. and introduce additional features that will eventually make it resemble OCaml.
Homework Structure
Our starting point is the example calculator written using PLY. Before anything else, make sure you know how to execute that calculator.
I've copied that calculator, and broken it into three files:
calclexer.py that has the scanner (lexer) specifications.
calcparser.py that has the parser specifications.
calc.py that has the main program that puts the other two modules together.
These three files are in simplecalc.zip, in a folder called SimpleCalc. As the second step, unpack this zip file, and make sure you can run the calculator (e.g. python calc.py). Compare this version with the example single-file specification in (1), so that you get an idea of how the modules were split up.
From SimpleCalc in (2) above, I derived up a more elaborate version, in elaboratecalc.zip. This calculators in (1) and (2) evaluated expressions as they were being parsed. In this elaborate version, the parsed expressions are first represented as a data structure called its Abstract Syntax Tree (AST). See the section on Calculuator AST in this handout for more details on this. This elaborate version adds two files to the simple calculator: calcast.py that defines the AST and has methods to evaluate it; and calcerror.py that consolidates the exception definitions used in this elaborate version.
Finally, we are ready to go from a calculator to a programming language. In this homework, we add a few language features; the resulting language is called Flatte(1). The result is not yet a programming language, but sets the stage.
See the section on Flatte(1) in this handout for more details on the new language features. In future assignments, we will continue to add features, deriving a series of languages Flatte(2), Flatte(3), etc. where the languages become progressively more sophisticated.
The stub of an interpreter for Flatte(1) is derived based on the elaborate calculator described in (3) above. The stub is in flatte1.zip, in a folder named Flatte1, containing the following files, all modified from the elaborate implementation of the calculator:
iflatte.py that has the main program that puts all the other modules together (modified from calc.py of ElaborateCalc)
flattelexer.py that has the scanner (lexer) specifications (modified from calclexer.py of ElaborateCalc)
flatteparser.py that has the parser specifications (modified from calcparser.py of ElaborateCalc)
flatteerror.py that has the exception definitions (modified from calcerror.py of ElaborateCalc)
flatteast.py that has the AST definitions (modified from calcast.py of ElaborateCalc)
Of these files, the first four are complete: you will not need to modify them. The last, flatteast.py defines the AST, but the eval method of some classes are left partially defined. Completing these methods will give you the expected interpreter for Flatte(1).
Abstract Syntax Tree for the Calculator
Recall that the calculator processes integer arithmetic expressions. The concrete syntax of these expressions is given in the parser specifications. After successfully parsing a string, we can represent the parsed expression as a tree that reflects the structure of the expression and its components. For the calculator this tree can be defined, for example, in OCaml as:
`type unop = UMINUS
type binop = PLUS | MINUS | MULTIPLY | DIVIDE
type expr = IntConst of int
         | Name of string
         | Unary of unop * expr
         | Binary of binop * expr * expr`
Python, unlike OCaml, does not directly support algebraic data structures such as expr above. So we implement this tree data structure using a set of classes: expr itself is implemented as an abstract class, called Expr and each kind of tree node (e.g. IntConst, Name, etc) is implemented as a subclass of expr (e.g. IntConstExpr, NameExpr, etc.). See calcast.py for the complete definition of these classes; in particular see the __init__ method of each class to find the set of fields in each instance of that class.
The input to the calculator are either expressions themselves (e.g. 1+2) or definitions (e.g. x = 1 + 2). We denote these inputs as statements which can also be represented by a tree data structure. In OCaml, this will look like:

`type stmt = Expr of expr
          | Assign of string * expr`
Again, in Python, we represent the above tree using three classes: Stmt, an abstract class representing any node in this tree; ExprStmt for representing the Expr nodes, and AssignStmt for representing the Assign nodes. See calcast.py for the complete definition of these classes.
One cool thing about this class-based representation of the AST is that we can define a method (called eval) in each node class to evaluate the tree rooted at that node. See the eval methods in calcast to see how the evaluation is done. The eval method returns the integer value of a given tree.

Flatte(1)
To get Flatte(1) from the calculator, we add the following to the expression language:
One new binary integer operator, mod
Boolean constants true and false
Boolean operators &&, || (both binary), and not (unary)
Comparison operators =, <>, <, >, <=, >= (all binary)
If-expression, of the form: if expression then expression else expression
Let-expression, of the form let name = expression in expression, where name is an identifier.
The syntax of these expressions is identical to those in OCaml. Moreover, the meaning of these expressions is very similar to that in OCaml, except for one simplification. OCaml expressions are strongly statically typed, and do not allow us to mix Boolean and Integer values in operations. In Flatte(1), we will allow Boolean values to occur in integer expressions (true will be treated as 1, and false as 0), and integer values to occur in Boolean expressions (0 will be treated as false and any non-zero integer value will be treated as true). A future version of Flatte will do run-time and compile-time type checking, and will get closer to OCaml in this regard, but not Flatte(1), not now.
Your Task
As stated earlier, flatte1.zip has 5 files needs to implement your interpreter. Of these files, flatteast.py, is the only one you will need to modify, but even that modification is needed only at certain places in that file.
The interpreter is built by completing the specification of all the eval method for all classes. For some classes, like IntConstExpr, which has not changed from the calculator, there is nothing to modify! For some simple expressions such as BoolConstExpr which represents boolean constants, which are new in Flatte(1), the eval method is already complete, so there's nothing to change either. But for other classes, such as BinaryExpr, you will need to add code to evaluate expressions that use the new operators introduced in Flatte(1). Look for methods where "Unimplemented" exception is raised, and those are the only methods that you will need to modify.

Grading
The maximum grade on this homework is 25 points. The grade will be assigned based on how much of Flatte(1) you can successfully process. The overall grading is split as follows: 10 points for complete implementation of Boolean operators and if-expression; 5 points for comparison operations; 10 points for let expression. As usual, please document your code, especially the sections that do something intricate. Code that is poorly structured and documented may not receive full credit.

Submission
Your submission will consist of a single Python program file, flatteast.py.
Submit your homework using Blackboard (see Homework #2 in Assignments area) before midnight of the due date.

Errata:
Link to PLY's example calculator was wrong. Fixed on Oct 14.
C.R. Ramakrishnan
Last modified: Sun Oct 14 15:06:18 EDT 2018
