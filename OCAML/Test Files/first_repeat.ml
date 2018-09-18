exception NoneSuch

let rec list_to_string = function
  | [] -> ""
  | x::xs -> string_of_int x ^ " " ^ list_to_string xs;;

let rec print_list = function
| [] -> print_string "\n"
| x :: xs -> print_int x; print_string " "; print_list xs

let rec contains_elem n= function
| [] -> false
| x :: xs -> if (x == n) then true else contains_elem n xs

let rec first_repeat = function
| [] -> raise NoneSuch
| x1 :: xs -> if (contains_elem x1 xs) then x1 else first_repeat xs

(*let () = Printf.printf "%d" (first_repeat [[1]; [1;2]; [1;2;3]; [1;2]; [1;4]]*)
print_string (list_to_string (first_repeat [[1]; [1;2]; [1;2;3]; [1;2]; [1;4]]));;
