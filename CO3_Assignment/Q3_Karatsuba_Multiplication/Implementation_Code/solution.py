def karatsuba(x,y,threshold=32):
    if x<0 or y<0:
        sign=-1 if (x<0)!=(y<0) else 1
        return sign*karatsuba(abs(x),abs(y),threshold)
    if x<10**threshold or y<10**threshold:return x*y
    m=max(len(str(x)),len(str(y)))//2;b=10**m
    a0,a1=divmod(x,b);c0,c1=divmod(y,b)
    z0=karatsuba(a1,c1,threshold);z2=karatsuba(a0,c0,threshold)
    z1=karatsuba(a0+a1,c0+c1,threshold)-z2-z0
    return z2*b*b+z1*b+z0
if __name__=="__main__":
    for x,y in [(1234,5678),(10**80+123,10**75+456)]:
        print("digits",len(str(x)),len(str(y)),"correct",karatsuba(x,y)==x*y)
