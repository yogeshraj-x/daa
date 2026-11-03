def merge_sort(a):
    if len(a)<=1:return a[:]
    m=len(a)//2; L=merge_sort(a[:m]); R=merge_sort(a[m:])
    out=[]; i=j=0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:out.append(L[i]);i+=1
        else:out.append(R[j]);j+=1
    return out+L[i:]+R[j:]
def quick_sort(a):
    a=a[:]; st={"comparisons":0,"depth":0,"partitions":[]}
    def rec(lo,hi,d):
        st["depth"]=max(st["depth"],d)
        if lo>=hi:return
        p=a[hi];i=lo
        for j in range(lo,hi):
            st["comparisons"]+=1
            if a[j]<=p:a[i],a[j]=a[j],a[i];i+=1
        a[i],a[hi]=a[hi],a[i];st["partitions"].append((i-lo,hi-i))
        rec(lo,i-1,d+1);rec(i+1,hi,d+1)
    rec(0,len(a)-1,1);return a,st
if __name__=="__main__":
    for name,x in [("random",[8,3,7,4,9,2,6,5,1]),("sorted",list(range(12))),("reverse",list(range(11,-1,-1)))]:
        q,s=quick_sort(x)
        print(name,"merge",merge_sort(x),"quick",q,"stats",s)
