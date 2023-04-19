print("Last update: 11/02/2021")

import numpy as np
import pandas as pd
import sys


### Negatively charged residues ###
Asp=list(map(int, input("Asp residue sites(use space as separator):   ").split()))
Glu=list(map(int, input("Glu residue sites(use space as separator):   ").split()))
### Positively charged residues ###
Lys=list(map(int, input("Lys residue sites(use space as separator):   ").split()))
Arg=list(map(int, input("Arg residue sites(use space as separator):   ").split()))
His=list(map(int, input("His residue sites(use space as separator):   ").split()))

totneg=(np.sum(len(Asp)+len(Glu)))

with open('SB.in', 'w')  as sb, open('SB.sh', 'w') as bs: 
 for n, i in enumerate(Asp):
  for j in Lys:
   print('distance D',str(i),'K',str(j),'_',2*n+1,' :',str(i),'@OD1 :',str(j),'@NZ out Asp', str(i),'-Lys', str(j),'.dat', sep='',file=sb)
   print('distance D',str(i),'K',str(j),'_',2*n+2,' :',str(i),'@OD2 :',str(j),'@NZ out Asp', str(i),'-Lys', str(j),'.dat', sep='',file=sb)
   print('Asp',str(i),'Lys',str(j),'=$(awk -f ./dat/SB.awk ','Asp',str(i),'-Lys',str(j),'.dat)', sep='', file=bs)
  for j in Arg:
   print('distance D',str(i),'R',str(j),'_',2*n+1,' :',str(i),'@OD1 :',str(j),'@NE out Asp', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance D',str(i),'R',str(j),'_',2*n+2,' :',str(i),'@OD1 :',str(j),'@NH1 out Asp', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance D',str(i),'R',str(j),'_',2*n+3,' :',str(i),'@OD1 :',str(j),'@NH2 out Asp', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance D',str(i),'R',str(j),'_',2*n+4,' :',str(i),'@OD2 :',str(j),'@NE out Asp', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance D',str(i),'R',str(j),'_',2*n+5,' :',str(i),'@OD2 :',str(j),'@NH1 out Asp', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance D',str(i),'R',str(j),'_',2*n+6,' :',str(i),'@OD2 :',str(j),'@NH2 out Asp', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('Asp',str(i),'Arg',str(j),'=$(awk -f ./dat/SB.awk ','Asp',str(i),'-Arg',str(j),'.dat)', sep='', file=bs)
  for j in His:
   print('distance D',str(i),'H',str(j),'_',2*n+1,' :',str(i),'@OD1 :',str(j),'@ND1 out Asp', str(i),'-His', str(j),'.dat', sep='',file=sb)
   print('distance D',str(i),'H',str(j),'_',2*n+2,' :',str(i),'@OD1 :',str(j),'@NE2 out Asp', str(i),'-His', str(j),'.dat', sep='',file=sb)
   print('distance D',str(i),'H',str(j),'_',2*n+3,' :',str(i),'@OD2 :',str(j),'@ND1 out Asp', str(i),'-His', str(j),'.dat', sep='',file=sb)
   print('distance D',str(i),'H',str(j),'_',2*n+4,' :',str(i),'@OD2 :',str(j),'@NE2 out Asp', str(i),'-His', str(j),'.dat', sep='',file=sb)
   print('Asp',str(i),'His',str(j),'=$(awk -f ./dat/SB.awk ','Asp',str(i),'-His',str(j),'.dat)', sep='', file=bs)
 for n, i in enumerate(Glu):
  for j in Lys:
   print('distance E',str(i),'K',str(j),'_',2*n+1,' :',str(i),'@OE1 :',str(j),'@NZ out Glu', str(i),'-Lys', str(j),'.dat', sep='',file=sb)
   print('distance E',str(i),'K',str(j),'_',2*n+2,' :',str(i),'@OE2 :',str(j),'@NZ out Glu', str(i),'-Lys', str(j),'.dat', sep='',file=sb)
   print('Glu',str(i),'Lys',str(j),'=$(awk -f ./dat/SB.awk ','Glu',str(i),'-Lys',str(j),'.dat)', sep='', file=bs)
  for j in Arg:
   print('distance E',str(i),'R',str(j),'_',2*n+1,' :',str(i),'@OE1 :',str(j),'@NE out Glu', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance E',str(i),'R',str(j),'_',2*n+2,' :',str(i),'@OE1 :',str(j),'@NH1 out Glu', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance E',str(i),'R',str(j),'_',2*n+3,' :',str(i),'@OE1 :',str(j),'@NH2 out Glu', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance E',str(i),'R',str(j),'_',2*n+4,' :',str(i),'@OE2 :',str(j),'@NE out Glu', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance E',str(i),'R',str(j),'_',2*n+5,' :',str(i),'@OE2 :',str(j),'@NH1 out Glu', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('distance E',str(i),'R',str(j),'_',2*n+6,' :',str(i),'@OE2 :',str(j),'@NH2 out Glu', str(i),'-Arg', str(j),'.dat', sep='',file=sb)
   print('Glu',str(i),'Arg',str(j),'=$(awk -f ./dat/SB.awk ','Glu',str(i),'-Arg',str(j),'.dat)', sep='', file=bs)
  for j in His:
   print('distance E',str(i),'H',str(j),'_',2*n+1,' :',str(i),'@OE1 :',str(j),'@ND1 out Glu', str(i),'-His', str(j),'.dat', sep='',file=sb)
   print('distance E',str(i),'H',str(j),'_',2*n+2,' :',str(i),'@OE1 :',str(j),'@NE2 out Glu', str(i),'-His', str(j),'.dat', sep='',file=sb)
   print('distance E',str(i),'H',str(j),'_',2*n+3,' :',str(i),'@OE2 :',str(j),'@ND1 out Glu', str(i),'-His', str(j),'.dat', sep='',file=sb)
   print('distance E',str(i),'H',str(j),'_',2*n+4,' :',str(i),'@OE2 :',str(j),'@NE2 out Glu', str(i),'-His', str(j),'.dat', sep='',file=sb)
   print('Glu',str(i),'His',str(j),'=$(awk -f ./dat/SB.awk ','Glu',str(i),'-His',str(j),'.dat)', sep='', file=bs)
 print('run', file=sb)
 print('rm -f SBmat.dat', file=bs)


 nl=r"\n"
 sp1=" %10s"
 sp2=" %10.4f" 
 spt1=sp1*totneg
 spt2=sp2*totneg
 print('printf "%10s',spt1,nl,'" " " ', end='', sep='', file=bs)
 for i in Asp:
  print('"Asp',str(i,),'" ', end=' ', sep='', file=bs)
 for j in Glu:
  print('"Glu',str(j,),'" ', end='', sep='', file=bs) 
 print('  >> SBmat.dat', file=bs)
 for k in Lys:
  print('printf "%10s',spt2,nl,'" "Lys',str(k),'" ', end='', sep='', file=bs)
  for i in Asp:
   print('"$Asp',str(i,), 'Lys',str(k),'" ',end=' ', sep='', file=bs)
  for j in Glu:
   print('"$Glu',str(j,), 'Lys', str(k),'" ',end=' ', sep='', file=bs)
  print(' >> SBmat.dat', file=bs)
 for l in Arg:
  print('printf "%10s',spt2,nl,'" "Arg',str(l),'" ', end='', sep='', file=bs)
  for i in Asp:
   print('"$Asp',str(i,), 'Arg',str(l),'" ',end=' ', sep='', file=bs)
  for j in Glu:
   print('"$Glu',str(j,), 'Arg', str(l),'" ',end=' ', sep='', file=bs)
  print(' >> SBmat.dat', file=bs)
 for m in His:
  print('printf "%10s',spt2,nl,'" "His',str(m),'" ', end='', sep='', file=bs)
  for i in Asp:
   print('"$Asp',str(i,), 'His',str(m),'" ',end=' ', sep='', file=bs)
  for j in Glu:
   print('"$Glu',str(j,), 'His', str(m),'" ',end=' ', sep='', file=bs)
  print(' >> SBmat.dat', file=bs)
 print('Rscript ./dat/SB.R', file=bs)
