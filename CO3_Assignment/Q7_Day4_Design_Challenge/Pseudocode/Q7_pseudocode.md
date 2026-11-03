# Q7 pseudocode — Count inversions
```text
COUNT-INV(A):
 if n<=1:return (A,0)
 split A into left and right
 (L,lc)=COUNT-INV(left); (R,rc)=COUNT-INV(right)
 i=0;j=0;cross=0;S=[]
 while i<len(L) and j<len(R):
   if L[i]<=R[j]: append L[i]; i++
   else: append R[j]; j++; cross += len(L)-i
 append remaining L and R
 return (S,lc+rc+cross)
```
