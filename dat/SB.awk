BEGIN {
  CUTOFF = 3.2
}

{
if (NF == 4)
 {
  if ($2 < CUTOFF || $3 < CUTOFF || $4 < CUTOFF)
   count++
 }

if (NF == 3)
 {
  if ($2 < CUTOFF || $3 < CUTOFF)
   count++
 }


  tot++
}
END {
   per = 100*count/tot
   print per
}
