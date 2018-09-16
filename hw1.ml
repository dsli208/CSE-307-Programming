(*Part 1 - indivisible*)
let rec indivisible i = function
| [] -> true
| x::xs -> ((x mod i != 0) && (indivisible i xs))

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
let rec poorsort = function
| [] -> ([], 0)
(*| x1 :: x2 :: xs -> if inorder(x1::x2::xs) then ((x1::x2::xs),0) else if (x1 > x2)*)

(*Part 6 - first_repeat*)
let rec contains_elem n= function
| [] -> false
| x :: xs -> if (x == n) then true else contains_elem n xs

let rec first_repeat = function
| [] -> raise NoneSuch
