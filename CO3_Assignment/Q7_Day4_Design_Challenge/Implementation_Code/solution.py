def count_inversions(a):
    def rec(x):
        if len(x)<=1:return x[:],0
        m=len(x)//2;L,lc=rec(x[:m]);R,rc=rec(x[m:])
        i=j=c=0;S=[]
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:S.append(L[i]);i+=1
            else:S.append(R[j]);j+=1;c+=len(L)-i
        return S+L[i:]+R[j:],lc+rc+c
    return rec(list(a))
def brute(a):
    return sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
if __name__=="__main__":
    for a in ([],[5],[1,2,3],[3,2,1],[2,4,1,3,5],[2,2,1]):
        x=count_inversions(a)[1];y=brute(a)
        print(a,"count",x,"baseline",y,"correct",x==y)
