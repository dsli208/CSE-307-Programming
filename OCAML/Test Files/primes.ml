let rec print_list = function
[] -> print_string "\n"
| x :: xs -> print_int x; print_string " "; print_list xs

let rec indivisible i = function
| [] -> true
| x::xs -> if (i mod x == 0) then false else (indivisible i xs)

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

print_list (primes 16);
