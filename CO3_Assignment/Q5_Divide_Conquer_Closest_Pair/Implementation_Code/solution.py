from math import hypot
def brute(P):
    best=float("inf");pair=None;c=0
    for i in range(len(P)):
        for j in range(i+1,len(P)):
            c+=1;d=hypot(P[i][0]-P[j][0],P[i][1]-P[j][1])
            if d<best:best,pair=d,(P[i],P[j])
    return best,pair,c
def closest_pair(P):
    if len(P)<2:return float("inf"),None,0
    px=sorted(P);py=sorted(P,key=lambda p:p[1])
    def rec(xs,ys):
        if len(xs)<=3:return brute(xs)
        mid=len(xs)//2;L=xs[:mid];R=xs[mid:];sx=R[0][0];ls=set(L)
        yl=[p for p in ys if p in ls];yr=[p for p in ys if p not in ls]
        dl,pl,cl=rec(L,yl);dr,pr,cr=rec(R,yr)
        best,pair=(dl,pl) if dl<=dr else (dr,pr);strip=[p for p in ys if abs(p[0]-sx)<best];c=cl+cr
        for i in range(len(strip)):
            j=i+1
            while j<len(strip) and strip[j][1]-strip[i][1]<best:
                c+=1;d=hypot(strip[i][0]-strip[j][0],strip[i][1]-strip[j][1])
                if d<best:best,pair=d,(strip[i],strip[j])
                j+=1
        return best,pair,c
    return rec(px,py)
if __name__=="__main__":
    P=[(2,3),(12,30),(40,50),(5,1),(12,10),(3,4),(8,8)]
    print("brute",brute(P));print("divide-conquer",closest_pair(P))
