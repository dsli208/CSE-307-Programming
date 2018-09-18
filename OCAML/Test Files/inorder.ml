(*let rec inorder_rec previous_lowest_num = function
| [] -> true (*end of the list*)
| x :: xs -> if (x < previous_lowest_num) then false
    else inorder_rec x xs

let rec inorder = function
| [] -> true (*only if the list sent in is ORIGINALLY empty*)
| x :: xs -> inorder_rec x xs*)

let rec inorder = function
| [] -> true (*How do you handle x2 being []?*)
| x1 :: [] -> true
| x1 :: x2 :: xs -> if (x1 > x2) then false else inorder (x2 :: xs)

let () = Printf.printf "%B" (inorder [2;5;4])
