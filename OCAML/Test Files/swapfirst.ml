let rec print_list = function
[] -> print_string "\n"
| x :: xs -> print_int x; print_string " "; print_list xs

let rec swapfirst = function
| [] -> []
| x :: [] -> x :: []
| x1 :: x2 :: xs -> if (x1 > x2) then (x2 :: x1 :: xs) else (x1 :: swapfirst (x2 :: xs))

let xs = (swapfirst [1;3;4;2]);;
print_list xs;;
