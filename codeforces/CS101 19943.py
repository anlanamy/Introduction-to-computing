#CS101 19943
n,m=map(int,input().split())
D=[[0]*n for i in range(n)]
A=[[0]*n for i in range(n)]
L=[[0]*n for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    D[a][a]+=1
    D[b][b]+=1
    A[a][b]=A[b][a]=1
for i in range(n):
    for j in range(n):
        L[i][j]=D[i][j]-A[i][j]
for i in range(n):
    print(' '.join([str(x) for x in L[i]]))