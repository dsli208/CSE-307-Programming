(*David S. Li - 110328771
CSE 307 HW 1*)

(*declaring NoneSuch exception for parts 6 and 7*)
exception NoneSuch

(*Part 1 - indivisible*)
let rec indivisible i = function
| [] -> true
| x::xs -> if (i mod x == 0) then false else (indivisible i xs)

(*Part 2 - prime*)


(*Part 3 - inorder*)
let rec inorder = function
| [] -> true (*How do you handle x2 being []?*)
| x1 :: x2 :: xs -> if (x1 > x2) then false else inorder (x2 :: xs)

(*Part 4 - swapfirst*)
let rec swapfirst = function
| [] -> []
| x1 :: x2 :: xs -> if (x1 > x2) then (x2 :: x1 :: xs) else swapfirst (x2 :: xs)

(*Part 5 - poorsort*)
let rec poorsort_rec i = function
| [] -> ([], i)
| x1 :: x2 :: xs -> if (x1 > x2) then poorsort_rec(x2 :: x1 :: xs, i + 1) else poorsort_rec(x2 :: xs, i)

let rec poorsort = function
| [] -> ([], 0)
| xs -> if inorder(xs) then ((xs),0) else poorsort_rec((xs, 0))

(*Part 6 - first_repeat*)
let rec contains_elem n= function
| [] -> false
| x :: xs -> if (x == n) then true else contains_elem n xs

let rec first_repeat = function
| [] -> raise NoneSuch
| x1 :: xs -> if contains_elem(x1 xs) then x1 else first_repeat xs

(*Part 7 - supdivisor*)
let rec factorial =
  if (x <= 0) then 1 else x * factorial(x - 1);;

let rec supdivisor_rec i =
 if (x mod 2**i == 0) then supdivisor_rec(x, i + 1) else (i - 1)

let rec supdivisor =
if (x < 0) then raise NoneSuch else supdivisor_rec(factorial(x), 0)
