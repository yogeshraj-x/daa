def minmax(a):
    if not a: raise ValueError("array must not be empty")
    count=0
    def rec(lo,hi):
        nonlocal count
        if lo==hi: return a[lo],a[lo]
        if hi==lo+1:
            count+=1
            return (a[lo],a[hi]) if a[lo]<=a[hi] else (a[hi],a[lo])
        m=(lo+hi)//2; x,X=rec(lo,m); y,Y=rec(m+1,hi)
        count+=2
        return min(x,y),max(X,Y)
    mn,mx=rec(0,len(a)-1)
    return mn,mx,count
def binary_search(a,x):
    lo,hi,c=0,len(a)-1,0
    while lo<=hi:
        m=(lo+hi)//2; c+=1
        if a[m]==x:return m,c
        c+=1
        if a[m]<x:lo=m+1
        else:hi=m-1
    return -1,c
if __name__=="__main__":
    a=[7,-2,9,4,1,12,0,5]
    print("min,max,comparisons:",minmax(a))
    s=sorted(a)
    for x in (-2,6,12):print("search",x,binary_search(s,x))
