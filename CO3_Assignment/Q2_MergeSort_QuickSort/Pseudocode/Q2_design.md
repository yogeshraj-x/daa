# Q2 — Merge Sort and Quick Sort
Merge Sort: if n<=1 return; split into equal halves; recursively sort both; merge in linear time. Recurrence 2T(n/2)+Theta(n)=Theta(n log n), auxiliary space Theta(n); decomposition is balanced and predictable.

Quick Sort (last-element Lomuto pivot): partition items <= pivot to left and larger items to right; recurse on both sides. Balanced recurrence is 2T(n/2)+Theta(n)=Theta(n log n); repeated 0:(n−1) splits yield T(n)=T(n−1)+Theta(n)=Theta(n^2), recursion depth Theta(n).

Experiment with random-like, sorted, reverse-sorted and duplicate-heavy arrays; record partition sizes, comparisons and max depth. Before choosing a sorting component, consider input size/order, duplicates, stability, memory, worst-case latency and cache behaviour. Merge Sort is stable/predictable but uses extra memory; Quick Sort is often in-place but pivot-sensitive.
