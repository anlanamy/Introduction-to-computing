#6
T,M=map(int,input().split())
l=[0]*(T+1)
copyl=l[:]
for i in range(M):
    t,m=map(int,input().split())
    if t<=T:
        for j in range(t,T+1):
            l[j]=max(copyl[j-t]+m,l[j])
        copyl=l[:]
print(l[T])