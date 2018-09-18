let rec sumlist = function
[] -> 0
| x::xs -> x + sumlist xs;;
