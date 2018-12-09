let rec matches xs ys = function
| ([], []) -> true
| (x :: [], y :: []) -> true
| (x :: xs, y :: ys) -> if (x == y) then (matches xs ys) else false


let palindrome xs = function
| [] -> true
| x :: [] -> true
| let ys = (reverse xs) in xs -> matches xs ys
