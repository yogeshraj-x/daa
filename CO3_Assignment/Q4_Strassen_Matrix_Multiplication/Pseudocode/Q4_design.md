# Q4 — Strassen Matrix Multiplication
For block matrices A11..A22 and B11..B22 compute seven products:
M1=(A11+A22)(B11+B22); M2=(A21+A22)B11; M3=A11(B12−B22); M4=A22(B21−B11); M5=(A11+A12)B22; M6=(A21−A11)(B11+B12); M7=(A12−A22)(B21+B22).
Reconstruct C11=M1+M4−M5+M7; C12=M3+M5; C21=M2+M4; C22=M1−M2+M3+M6. Conventional block multiplication uses eight products; Strassen uses seven. Pad non-power-of-two dimensions with zeros to a square power of two and crop the output. T(n)=7T(n/2)+Theta(n^2)=Theta(n^2.807). Conventional is Theta(n^3). Additions, allocations, recursion and padding may make conventional multiplication faster for small matrices.
