# CSE 307: Principles of Programming Languages - Fall 2018
## Homework #3 - Due: Mon., Nov 10
In this assignment, you will fill parts of an interpreter for Flatte, an OCaml-like functional programming language. For this homework, we will start with template built upon solution to HW2, and introduce additional features.

## Homework Structure
There are **two** possible extensions to HW2:
1. Addition of functions and data structures.
More specifically, this extension adds **function definitions** using expressions of the form `fun x -> e` and **function calls** using expressions of the form `e1 e2;` and a **pair data structure**, for representing pairs of values of the form `(v1, v2)` and two accessor operators `fst` and `snd` (to access `v1` and `v2`, respectively, from `(v1, v2)`).

2. Addition of side-effecting operations of `ref` (create new cells in store), `!` (dereference locations in store), `:=` (assign value to a location), and `;` (evaluate expressions in a sequence).

For this homework, you may implement **either of the two examples**.

For functions and data structures, start with `flatte2.zip`, and add/modify `eval` functions in `flatteast.py`. As in HW2, look for places where `Unimplemented` exception is thrown.

For references and assignments, start with `flatte3.zip`, and add/modify `eval` functions in `flatteast.py`. As in HW2, look for places where `Unimplemented` exception is thrown.

Both packages contain the following files (same structure as in HW2):
* `iflatte.py` that has the main program that puts all the other modules together
* `flattelexer.py` that has the scanner (lexer) specifications
* `flatteparser.py` that has the parser specifications
* `flatteerror.py` that has the exception definitions
* `flatteast.py` that has the AST definitions

Of these files, *the first four are complete: you will not need to modify them*. The last, `flatteast.py` defines the AST, but the eval method of some classes are left partially defined. Completing these methods will give you the expected interpreter for Flatte(1).

## Option 1: Adding functions and data structures
Functions are added to Flatte(1) of HW2 via the addition of two expressions:
1. Function Definition. Syntactically, this looks like `fun x -> e` where `x` is a name, representing the formal parameter of the function and `e` is an expression, representing the body of the function. In the abstract syntax tree, this is represented by `FunDefExpr` class, with two main fields: `param` for the formal parameter, and `body` for the body.
2. Function Application. Syntactically, this looks like ``(e1 e2)`` where `e1` is the function to be called, and `e2` is the argument passed to that call. In the abstract syntax tree, this is represented by `ApplyExpr` class, with two main fields: `funexpr` for the function to be called, and `argexpr` for the argument to be passed.

Your task in this HW is to fill the `eval` functions of these two classes such that expressions with function definitions and calls can be successfully evaluated. Your implementation should be consistent with static scoping.

Pair data structures are added to Flatte(1) of HW2 via the addition of three expressions:
1. Pair Construction. Syntactically, this looks like `(e1, e2)` where `e1` and `e2` define the first and second elements of the pair, respectively. In the abstract syntax tree, this is represented by `PairExpr` class, with two main fields: `arg1` and `arg2` to represent the first and second elements of the pair.
2. Access operators `fst` and `snd`. Syntactically, `fst` and `snd` are unary operators. In the abstract syntax tree, they are represented by instances of `UnaryExpr` class with `uop` equal to `fst` and `snd`, respectively.

Your task in this HW is to fill the `eval` complete the `eval` of these `UnaryExpr` classes such that expressions using the pair data structure can be successfully evaluated.

### Assumptions and Minor Changes
You may assume that the input it a syntactically and semantically valid expression. That is, not only will the input be successfully parsed, there will be no semantic error in performing the operations. For instance, fst will always operate on a pair, e1 in (e1 e2) will always be a function, e in !e will be a location, etc.
The front end of the interpreter accepts expressions ending in ";;" (two semicolons, as in OCAML).
You may also enter "#use filename" at the prompt, which will make the parser read and build an AST for the contents of the given filename. If the file contains a sequence of expressions, they will all be evaluated in order, and their values printed to console.
A syntactic sugar for function definitions is implemented in the parser in flatte2.zip. This accepts OCAML-style definitions of the form let f x = e1 in e2, in addition to let f = fun x -> e1 in e2. In fact expressions of the first form are converted to the second form by the parser.
These changes may make it simpler to write test cases for your homework.

## Option 2: Adding references and assignments
Mutable store is added to Flatte(1) of HW2 via the addition of four expressions:
1. Reference creation. Syntactically, this looks like `ref e` where `e` is an expression. This creates a new location in store initialized with the value of `e`. The value of ref `e` itself is the new location created. In the abstract syntax tree, this is represented by an instance of the `UnaryExpr` with `uop = "ref"`.
2. Dereference. Syntactically, this looks like `! e` where `e` is an expression. This evaluates `e`, which should be a location, say `l`. Then the value of `! e` is the value stored at `l`. In the abstract syntax tree, this is represented by an instance of the `UnaryExpr` with `uop = "!"`.
3. Assignment. Syntactically, this looks like `e1 := e2` where `e1` and `e2` are expressions. This evaluates `e1`, which should be a location, say `l`; then `e2` to some value, say `v`. Then the store is updated such that location `l` is changed to contain value `v`. In the abstract syntax tree, this is represented by `AssignExpr` class, with two main fields: `lhs` for the left hand side expression (`e1`), and `rhs` for the right hand side expression (`e2`).
4. Sequence. Syntactically, this looks like `e1 ; e2` where `e1` and `e2` are expressions. This evaluates `e1`, and then `e2`; The value of `e1; e2` is the value of `e2`.  In the abstract syntax tree, this is represented by `SequenceExpr` class, with two main fields: first for the left hand side expression (`e1`), and next for the right hand side expression (`e2`).

Note that, when operations with side effects are introduced into the language, the definition of existing expressions change to take the store into account. In the files given in `flatte3.zip`, the `eval` function has been modified to take *two* arguments: `env`, the environment (as in the old interpreter), and `store`, the structure representing the store (which maps locations to values). The meaning of all existing expressions has been modified to take into account the order of operations. Calls to `eval` return a pair ``(s, v)``, where `s` is the new store resulting from the evaluation, and `v` is the value of the expression evaluated.

Your task in this HW is to fill the `eval` functions corresponding to the above four operations such that expressions with references, dereferences, assignments, and sequences can be successfully evaluated.

## Grading
You may choose to complete either Option 1 or Option 2. The maximum grade on this homework is 25 points. The grade will be assigned based on how much of Flatte(2) [Option 1] or Flatte(3) [Option 2] you can successfully process. As usual, **please document your code, especially the sections that do something intricate**. Code that is poorly structured and documented may not receive full credit.

## Submission
You may complete either Option 1 or Option 2 described above.
Your submission will consist of a single Python program file, `flatteast.py`.

Submit your homework using Blackboard (see Homework #3 in Assignments area) before midnight of the due date.

Errata:
Broken links for `flatte2.zip` and `flatte3.zip` have been fixed. (Dec 5, 11:30am).
C.R. Ramakrishnan
Last modified: Wed Dec 5 11:32:45 EST 2018
