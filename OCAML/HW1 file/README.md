# CSE 307: Principles of Programming Languages - Fall 2018
## Homework #1
## Due: Tue., Sep 18
This is a programming assignment. You are expected to write OCaml functions for the problems described below. The solution for each question may have multiple OCaml functions: a main one which uses the rest as helpers. You will place all the OCaml functions you write to solve the following problems in a single program file. Submit the file using the usual handin procedure (described at the end of this handout).
Important!
Each function above should be written in functional style in OCAML (i.e. without using OCAML's imperative features such as references).
Unless otherwise noted, you should not use any OCAML library functions for the problems below.
You may define and use additional (helper) functions.
Unless otherwise noted, you need not consider the time or space efficiency of your functions.
The Assignment:
[5 points] Write a function indivisible that takes an integer i and a list of integers l, and returns false if and only if some integer in l divides i. For instance, `indivisible(15, [2;3;4])` is false, but `indivisible(15, [2;4;8])` is true.
[5 points] Using indivisible, write a function primes that takes a positive integer and returns the list of all prime numbers smaller than or equal to that integer. For instance, primes(16) should `return [2;3;5;7;11;13]`. (If it returns a permutation of this list, e.g. `[13;11;7;5;3;2]`, that is ok too).
Hint: Consider `indivisible(16, primes(15))`. Is it true or false? How does this affect `primes(16)`?

Now consider `indivisible(17, primes(16))`. Is it true or false? How does this affect `primes(17)`?

Write a function `inorder` that takes a list l, and returns true if the sequence of elements in l are all in ascending order.
For instance, `inorder [2;3;4]` and `inorder [2;4;8;16]` are true, but `inorder [4;3;2]` and `inorder [2;4;3]` are false.

Note that `inorder` will be true for empty and singleton lists.

Write a function swapfirst that takes a list l, and returns another list l' obtained by swapping the first two elements in l that are not in ascending order; and l itself if the list is inorder (as per prev. question).
For instance,

swapfirst [4;3;2] should return [3;4;2];
swapfirst [3;4;2] should return [3;2;4];
swapfirst [3;2;4] should return [2;3;4];
swapfirst [2;3;4] should return [2;3;4] itself.
Write a function poorsort that takes a list l and sorts it using swapfirst (and, if necessary, inorder). More specifically, poorsort l should return a pair (s, n), where s is the sorted version of l, and n is the number of swaps done to sort l to s.
For instance,

poorsort [3;4;2] should return ([2;3,4], 2);
poorsort [3;2;4] should return ([2;3,4], 1); and
poorsort [2;3;4] should return ([2;3,4], 0).
Write a function first_repeat, with signature '' a list −> ''a, that returns the first element in the given list that repeats in that list. If there is no element that repeats, the function will end with raising exception NoneSuch. For example:
first_repeat([1;1;2;3]) should return 1.
first_repeat([1;2;3;2;3;4]) should return 2.
first_repeat([1;2;3;3;3;3;1]) should return 1.
first_repeat([1;2;3;4]) should raise exception NoneSuch.
Write a function supdivisor, with signature int −> int, that, given a positive integer n, returns the largest number k such that 2k divides n!. If n is negative, your function should raise exception NoneSuch.
For instance,

if the input n = 4, n! = 24, 8 is the largest power of 2 that divides 24, and hence the output k = 3.
if the input n = 10, n! = 3,628,800, 256 is the largest power of 2 that divides it, and hence the output k = 8.
Important: For full credit, your function should work correctly for reasonably large values of n.

Grading:
It is expected that each function will take 2-10 lines of code. Complicated function definitions will not get the full grade unless accompanied by comments documenting it. If the function does not work correctly as specified, your grade will depend largely on whether what is written is understandable.
All problems are worth 5 points. The maximum score on this homework is 35 points.

Submission:
Place the definition of each function (and any helpers they may use) in a single source file called hw1.ml.
Any tests you ran may also be placed in the same file. Document complex function definitions.
Submit your homework file by filling out the Homework 1 Submission Form on Blackboard (Assignments area).
Corrections and other changed from original handout:
Thu Sep 6 06:36:36 -- Original version.
Tue Sep 11 07:15:21 -- Added more detailed submission instructions. The original version only had the sentence about submission via blackboard.
C.R. Ramakrishnan
Last modified: Tue Sep 11 07:15:21 EDT 2018
