#4
n,m=map(int,input().split())
board=[[0]*(m+2)]+[[0]+[int(x) for x in input().split()]+[0] for j in range(n)]+[[0]*(m+2)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
count=0
numcount=[4,2,0,-2,-4]
def dfs(i,j):
    global count
    if board[i][j]!=1:
        return
    board[i][j]=2
    num=0
    for s in range(4):
        if board[i+dx[s]][j+dy[s]]==2:
            num+=1
    count+=numcount[num]
    for s in range(4):
        dfs(i+dx[s],j+dy[s])
for i in range(1,n+1):
        for j in range(1,m+1):
            if board[i][j]==1:
                dfs(i,j)
print(count)