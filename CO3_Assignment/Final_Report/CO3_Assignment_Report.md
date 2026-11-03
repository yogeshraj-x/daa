# CSA06 — Assignment 3 (CO3): Divide and Conquer
**Student:** Yogeshraj M V | **Register No.:** 1925260173  
**Submission type:** Solo adaptation. The supplied brief specifies pair work; faculty approval is required.

## Abstract
This submission implements tournament Max/Min, Binary Search, Merge Sort, Quick Sort, Karatsuba multiplication, Strassen matrix multiplication, Closest Pair, Median of Medians, Meet-in-the-Middle Subset Sum, and a selected Day-4 challenge: merge-based inversion counting.

## Complexity summary
| Topic | Recurrence / complexity |
|---|---|
| Max/Min | 2T(n/2)+2; 3n/2−2 comparisons for powers of two |
| Binary Search | T(n/2)+O(1); O(log n) |
| Merge Sort | 2T(n/2)+Theta(n); Theta(n log n) |
| Quick Sort | average Theta(n log n), worst Theta(n^2) |
| Karatsuba | 3T(n/2)+Theta(n); Theta(n^1.585) |
| Strassen | 7T(n/2)+Theta(n^2); Theta(n^2.807) |
| Closest Pair | 2T(n/2)+O(n); O(n log n) |
| Median of Medians | T(n/5)+T(7n/10)+O(n); O(n) worst case |
| Meet-in-the-Middle | O(n*2^(n/2)) time; O(2^(n/2)) space |
| Inversion counting | 2T(n/2)+Theta(n); Theta(n log n) |

## Experimental protocol
Run each script using the same Python version and machine. Use identical inputs for competing algorithms. Warm up, repeat trials, report median and spread, and document CPU, OS, Python version, input size and random seed. Operation counts are more reproducible than single-run wall-clock timings.

## Technical observations
Balanced decomposition controls recursion-tree height; repeated Quick Sort imbalance can cause a linear-depth tree. Karatsuba and Strassen reduce recursive multiplication counts but add overhead, so practical crossover must be measured. Closest Pair needs a boundary strip for cross-half candidates; geometric packing bounds relevant neighbours. Median of Medians guarantees worst-case linear selection by ensuring a sufficiently good pivot. Meet-in-the-Middle reduces exponential work at the cost of exponential memory. Inversion counting reuses merge to count cross-half pairs.

## Evidence and limitations
The implementation and pseudocode are in the question folders. Output_Screenshots folders currently contain instructions only: capture genuine terminal screenshots after running each script. Machine-specific benchmark tables/graphs are not claimed because no hardware measurements have been supplied. The requested DOCX report format remains to be exported from this Markdown report.

The brief requires two-person participation, separate independent Day-4 proposals, and a contribution record. Only one student was identified; no second-student or joint contribution is invented. Seek faculty approval for individual submission.
