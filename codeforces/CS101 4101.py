#CS101 4101
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfsr(i,j):
    if l[i][j]!='r':
        return
    l[i][j]='R'
    for s in range(4):
        dfsr(i+dx[s],j+dy[s])

def dfsb(i,j):
    if l[i][j]!='b':
        return
    l[i][j]='B'
    for s in range(4):
        dfsb(i+dx[s],j+dy[s])
         
T=int(input())
for i in range(T):
    N=int(input())
    l=[[0]*(N+2)]+[[0]+list(input())+[0] for i in range(N)]+[[0]*(N+2)]
    countr=0
    countb=0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if l[i][j]=='r':
                countr+=1
                dfsr(i,j)
            if l[i][j]=='b':
                countb+=1
                dfsb(i,j)
    print(countr,countb)