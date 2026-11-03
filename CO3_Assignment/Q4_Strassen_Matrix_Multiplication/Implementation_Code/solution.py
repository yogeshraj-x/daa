def conventional(A,B):
    if len(A[0])!=len(B):raise ValueError("incompatible dimensions")
    C=[[0]*len(B[0]) for _ in A]
    for i in range(len(A)):
        for k in range(len(B)):
            for j in range(len(B[0])):C[i][j]+=A[i][k]*B[k][j]
    return C
def add(A,B):return [[x+y for x,y in zip(r,s)] for r,s in zip(A,B)]
def sub(A,B):return [[x-y for x,y in zip(r,s)] for r,s in zip(A,B)]
def split(A):
    n=len(A);h=n//2
    return ([r[:h] for r in A[:h]],[r[h:] for r in A[:h]],[r[:h] for r in A[h:]],[r[h:] for r in A[h:]])
def join(a,b,c,d):return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]
def strassen(A,B,cutoff=2):
    n=len(A)
    if n<=cutoff:return conventional(A,B)
    a,b,c,d=split(A);e,f,g,h=split(B)
    m1=strassen(add(a,d),add(e,h),cutoff);m2=strassen(add(c,d),e,cutoff)
    m3=strassen(a,sub(f,h),cutoff);m4=strassen(d,sub(g,e),cutoff)
    m5=strassen(add(a,b),h,cutoff);m6=strassen(sub(c,a),add(e,f),cutoff)
    m7=strassen(sub(b,d),add(g,h),cutoff)
    return join(add(sub(add(m1,m4),m5),m7),add(m3,m5),add(m2,m4),add(add(sub(m1,m2),m3),m6))
def strassen_any(A,B):
    n,m,p=len(A),len(B),len(B[0]);size=1
    if not A or not B or len(A[0])!=m:raise ValueError("invalid dimensions")
    while size<max(n,m,p):size*=2
    X=[[0]*size for _ in range(size)];Y=[[0]*size for _ in range(size)]
    for i in range(n):
        for j in range(m):X[i][j]=A[i][j]
    for i in range(m):
        for j in range(p):Y[i][j]=B[i][j]
    Z=strassen(X,Y)
    return [r[:p] for r in Z[:n]]
if __name__=="__main__":
    A=[[1,2,3],[4,5,6]];B=[[7,8],[9,10],[11,12]]
    print("conventional",conventional(A,B));print("Strassen",strassen_any(A,B))
    print("correct",conventional(A,B)==strassen_any(A,B))
