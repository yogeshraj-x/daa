def select_k(a,k):
    if not 0<=k<len(a):raise IndexError("k out of range")
    if len(a)<=5:return sorted(a)[k]
    groups=[sorted(a[i:i+5]) for i in range(0,len(a),5)]
    meds=[g[len(g)//2] for g in groups]
    p=select_k(meds,len(meds)//2)
    lo=[x for x in a if x<p];eq=[x for x in a if x==p];hi=[x for x in a if x>p]
    if k<len(lo):return select_k(lo,k)
    if k<len(lo)+len(eq):return p
    return select_k(hi,k-len(lo)-len(eq))
def quickselect(a,k):
    x=a[:];lo=0;hi=len(x)-1
    while lo<=hi:
        p=x[hi];i=lo
        for j in range(lo,hi):
            if x[j]<=p:x[i],x[j]=x[j],x[i];i+=1
        x[i],x[hi]=x[hi],x[i]
        if i==k:return x[i]
        if i<k:lo=i+1
        else:hi=i-1
    raise IndexError("k out of range")
if __name__=="__main__":
    a=[12,3,5,7,4,19,26,1,8,2,11,6,10]
    for k in (0,5,len(a)-1):print(k,select_k(a,k),quickselect(a,k),sorted(a)[k])
