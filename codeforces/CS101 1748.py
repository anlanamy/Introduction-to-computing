#CS101 1748
n,m=map(int,input().split())
while m+n!=0:
    l=[1]*n
    i=0
    j=m
    s=n
    while s!=1:
        if l[i]==1:
            j-=1
            if j==0:
                l[i]=0
                s-=1
                j=m
            i+=1
            i=i%n
        else:
            i+=1
            i=i%n
    print(l.index(1)+1)
    n,m=map(int,input().split())