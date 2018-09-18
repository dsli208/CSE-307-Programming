exception NoneSuch
let rec factorial x =
  if (x <= 0) then 1 else x * factorial(x - 1);;

let rec supdivisor_rec x i =
 if (x mod (int_of_float (2.0 **(float_of_int i))) == 0) then (supdivisor_rec x (i + 1)) else (i - 1)

let rec supdivisor x =
if (x < 0) then raise NoneSuch else (supdivisor_rec (factorial x) 0)

let () = Printf.printf "%d" (supdivisor (-10))
