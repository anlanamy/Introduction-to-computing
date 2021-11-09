#CS101 19942
def con(A,B,p,q):
    c=0
    for i in range(p):
        for j in range(q):
            c+=A[i][j]*B[i][j]
    return c
m,n,p,q=map(int,input().split())
A=[]
B=[]
C=[[0]*(n+1-q) for i in range(m+1-p)]
for i in range(m):
    A.append([int(x) for x in input().split()])
for i in range(p):
    B.append([int(x) for x in input().split()])
for i in range(m+1-p):
    for j in range(n+1-q):
        D=[A[r][j:j+q] for r in range(i,i+p)]
        C[i][j]=con(D,B,p,q)
for i in range(m+1-p):
    print(' '.join([str(x) for x in C[i]]))