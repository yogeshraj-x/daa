from bisect import bisect_left
def subset_sums(a):
    s=[0]
    for x in a:s += [v+x for v in s]
    return s
def mitm(a,target):
    m=len(a)//2;L=subset_sums(a[:m]);R=sorted(subset_sums(a[m:]))
    for x in L:
        i=bisect_left(R,target-x)
        if i<len(R) and R[i]==target-x:return True,(x,R[i])
    return False,None
def brute(a,target):return any(x==target for x in subset_sums(a))
if __name__=="__main__":
    a=[3,7,1,8,4,10,2,6];t=19
    print("MITM",mitm(a,t));print("brute",brute(a,t))
