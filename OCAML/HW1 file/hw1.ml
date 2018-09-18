(*David S. Li - 110328771
CSE 307 HW 1*)

(*declaring NoneSuch exception for parts 6 and 7*)
exception NoneSuch

(*Part 1 - indivisible*)
let rec indivisible i = function
| [] -> true
| x::xs -> if (i mod x == 0) then false else (indivisible i xs)

(*Part 2 - prime*)
(*generates a list of numbers between 2 and the number originally specified*)
let rec generate_list top_bound = function (*x, implicit arg, should start at 2*)
| x -> if (x > top_bound) then [] else (x :: (generate_list top_bound (x + 1)))

(*finds prime numbers less than the number originally specified*)
(*params: x - originally specified number, prime_nos - list of prime numbers, nos - see below*)
let rec primes_rec x prime_nos = function (*nos - short for numbers between 2 and x (inclusive) is implicit*)
| [] -> prime_nos
| n :: nos -> if (indivisible n (generate_list (n - 1) 2)) then (primes_rec x (n::prime_nos) nos) else (primes_rec x prime_nos nos)

let primes = function
| x -> (primes_rec x [] (generate_list x 2));;

(*Part 3 - inorder*)
let rec inorder = function
| [] -> true (*How do you handle x2 being []?*)
| x1 :: [] -> true
| x1 :: x2 :: xs -> if (x1 > x2) then false else inorder (x2 :: xs)

(*Part 4 - swapfirst*)
let rec swapfirst = function
| [] -> []
| x :: [] -> x :: []
| x1 :: x2 :: xs -> if (x1 > x2) then (x2 :: x1 :: xs) else (x1 :: swapfirst (x2 :: xs))

(*Part 5 - poorsort*)
let rec poorsort_rec i = function
| [] -> ([], i)
| x :: [] -> (x :: [], i)
| x1 :: x2 :: xs -> let (a,b) = (poorsort_rec i (x2::xs)) in if (x1 > x2) then (poorsort_rec (i + 1) (x2 :: x1 :: xs)) else ((x1::a), b)

let rec poorsort = function
| [] -> ([], 0)
| xs -> if (inorder xs) then ((xs),0) else (poorsort_rec 0 xs)


(*Part 6 - first_repeat*)
let rec contains_elem n= function
| [] -> false
| x :: xs -> if (x == n) then true else contains_elem n xs

let rec first_repeat = function
| [] -> raise NoneSuch
| x1 :: xs -> if contains_elem x1 xs then x1 else first_repeat xs

(*Part 7 - supdivisor*)
let rec factorial x =
  if (x <= 0) then 1 else x * factorial(x - 1);;

let rec supdivisor_rec x i =
 if (x mod (int_of_float (2.0 **(float_of_int i))) == 0) then (supdivisor_rec x (i + 1)) else (i - 1)

let rec supdivisor x =
if (x < 0) then raise NoneSuch else (supdivisor_rec (factorial x) 0)
