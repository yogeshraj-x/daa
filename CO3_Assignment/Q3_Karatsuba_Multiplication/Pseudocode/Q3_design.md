# Q3 — Karatsuba Multiplication
Split x=a*10^m+b and y=c*10^m+d. Compute z0=b*d, z2=a*c, z1=(a+b)(c+d)-z2-z0. Product = z2*10^(2m)+z1*10^m+z0.

```text
KARATSUBA(x,y):
 if either operand is small: return x*y
 split both operands at m digits into high and low parts
 z0=KARATSUBA(lowX,lowY)
 z2=KARATSUBA(highX,highY)
 z1=KARATSUBA(highX+lowX,highY+lowY)-z2-z0
 return z2*10^(2m)+z1*10^m+z0
```
T(n)=3T(n/2)+Theta(n)=Theta(n^log2(3))≈Theta(n^1.585), compared with schoolbook Theta(n^2). Better asymptotic complexity may lose on small inputs because recursion, splitting, allocations and additions have overhead. Crossover is implementation- and machine-dependent; measure repeated trials.
