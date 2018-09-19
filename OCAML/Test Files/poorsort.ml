let rec inorder = function
| [] -> true (*How do you handle x2 being []?*)
| x1 :: [] -> true
| x1 :: x2 :: xs -> if (x1 > x2) then false else (inorder (x2 :: xs))

let rec print_list = function
[] -> print_string "\n"
| x :: xs -> print_int x; print_string " "; print_list xs

let rec poorsort_rec i = function
| [] -> ([], i)
| x :: [] -> (x :: [], i)
| x1 :: x2 :: xs -> let (a,b) = (poorsort_rec i (x2::xs)) in if (x1 > x2) then (poorsort_rec (i + 1) (x2 :: x1 :: xs)) else ((x1::a), b)

let rec poorsort_done = function
| (a, b) -> if inorder a then (a, b) else poorsort_done (poorsort_rec b a)

let rec poorsort = function
| [] -> ([], 0)
| xs -> if (inorder xs) then ((xs),0) else poorsort_done (poorsort_rec 0 xs)

let (list, i_ret) = poorsort [3;2;4];;
print_list list;;
print_int i_ret;;
