# Q1 — Max/Min and Binary Search
## Tournament Max/Min
```text
MINMAX(A,lo,hi):
 if lo==hi: return (A[lo],A[lo])
 if hi==lo+1: compare once; return ordered pair
 mid=(lo+hi)//2
 (mn1,mx1)=MINMAX(A,lo,mid)
 (mn2,mx2)=MINMAX(A,mid+1,hi)
 return (min(mn1,mn2),max(mx1,mx2))
```
Each recursive subproblem returns its local minimum and maximum; combine with two comparisons. For n a power of two, T(n)=2T(n/2)+2 and T(1)=0, giving 3n/2−2 comparisons. Two independent scans need 2n−2. Test singleton, pairs, odd/even lengths, duplicates, negatives, sorted/reversed.

## Binary Search
Precondition: sorted ascending array.
```text
BINARY-SEARCH(A,x):
 low=0; high=n-1
 while low<=high:
   mid=(low+high)//2
   if A[mid]==x: return mid
   if A[mid]<x: low=mid+1
   else: high=mid-1
 return NOT_FOUND
```
Each comparison eliminates the half that cannot contain x. Stop when found or low>high. T(n)=T(n/2)+O(1)=O(log n), iterative space O(1). Test first/middle/last, absent keys, empty array and duplicates.
