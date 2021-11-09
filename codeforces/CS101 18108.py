#CS101 18108
dx=[0,0,1,1,1,-1,-1,-1]
dy=[1,-1,1,0,-1,1,0,-1]
def dfs(i,j):
    if l[i][j]!='W':
        return
    l[i][j]='M'
    for s in range(8):
        dfs(i+dx[s],j+dy[s])
            
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    l=[[0]*(M+2)]+[[0]+list(input())+[0] for i in range(N)]+[[0]*(M+2)]
    p=[[0]*(M+2) for i in range(N+2)]
    ans=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if l[i][j]=='W':
                ans+=1
                dfs(i,j)
    print(ans)