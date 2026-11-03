# Q6 — Advanced Divide and Conquer
## Median of Medians
Partition into groups of five; sort each group and collect medians. Recursively select the median of these medians as pivot. Partition input into less/equal/greater; recurse only into the rank-containing side, adjusting k. Worst-case recurrence T(n)<=T(n/5)+T(7n/10)+O(n)=O(n). Compare with QuickSelect (expected O(n), worst O(n^2)) and a fixed poor pivot (worst O(n^2)). Pivot quality controls the fraction discarded each round.

## Meet-in-the-Middle Subset Sum
Split n values into halves. Generate every subset sum for each half (about 2^(n/2)); sort one list. For each sum s in the other, binary-search target−s. Time O(n*2^(n/2)) including sorting, space O(2^(n/2)). This is a time-memory trade-off versus O(2^n) full enumeration.
