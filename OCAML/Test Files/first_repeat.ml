exception NoneSuch

let rec contains_elem n= function
| [] -> false
| x :: xs -> if (x == n) then true else contains_elem n xs

let rec first_repeat = function
| [] -> raise NoneSuch
| x1 :: xs -> if (contains_elem x1 xs) then x1 else first_repeat xs

let () = Printf.printf "%d" (first_repeat [1;2;3;4])
