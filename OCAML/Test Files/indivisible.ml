(* fix unbound i problem*)
let rec indivisible i = function
| [] -> true
| x::xs -> if (i mod x == 0) then false else (indivisible i xs)

let () = Printf.printf "%B" (indivisible 15 [2;4;6])
