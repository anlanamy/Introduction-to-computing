#CS101 1810
L,M=map(int,input().split())
l=[1]*(L+1)
for i in range(M):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        l[j]=0
print(sum(l))