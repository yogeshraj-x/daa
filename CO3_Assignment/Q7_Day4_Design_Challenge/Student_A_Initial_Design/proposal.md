# Initial design record — single-student adaptation
Student: Yogeshraj M V (1925260173). The brief requires two independent proposals; only one student was provided, so no two-person independent design stage is claimed.
Chosen challenge: count inversions (i<j and A[i]>A[j]). Proposed split: divide array into halves; recursively count within each half; count cross inversions while merging sorted halves. Base case length <=1 returns zero.
