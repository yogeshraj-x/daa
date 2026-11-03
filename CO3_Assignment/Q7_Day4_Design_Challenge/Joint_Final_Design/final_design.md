# Q7 — Design challenge: Count inversions
Solo-authored final design adaptation; not a jointly authored pair design.

An inversion is a pair (i,j), i<j, A[i]>A[j]. Divide the array into halves; recursively count left and right inversions. During merge, when right[j]<left[i], add len(left)-i because every remaining left element forms a cross inversion with right[j]. Return sorted array and total count.

Pseudocode:
```text
COUNT(A):
 if n<=1:return (A,0)
 (L,x)=COUNT(left half); (R,y)=COUNT(right half)
 merge L,R into S; cross=0
 whenever R[j]<L[i]: cross += len(L)-i; append R[j]
 otherwise append L[i]
 append remaining values
 return (S,x+y+cross)
```
Correctness: each inversion is left-only, right-only, or cross-half; recursive calls count the first two, merge counts the third. T(n)=2T(n/2)+Theta(n)=Theta(n log n), space Theta(n). Brute force baseline is Theta(n^2). Test sorted (0), reverse (n(n−1)/2), duplicates (strict >), empty, singleton and mixed arrays.
