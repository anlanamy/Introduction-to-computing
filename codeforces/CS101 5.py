#CS101 12560
def game(board,x,y):
    c=board[x-1][y-1]+board[x-1][y]+board[x-1][y+1]+board[x][y-1]+board[x][y+1]+board[x+1][y-1]+board[x+1][y]+board[x+1][y+1]
    if board[x][y]==1:
        if c<2 or c>3:
            return 0
        else:
            return 1
    else:
        if c==3:
            return 1
        else:
            return 0
n,m=map(int,input().split())
board=[[0]*(m+2)]+[[0]+[int(x) for x in input().split()]+[0] for j in range(n)]+[[0]*(m+2)]
output=[[0]*m for x in range(n)]
for i in range(n):
    for j in range(m):
        output[i][j]=game(board,i+1,j+1)
for y in range(n):
    print(' '.join([str(x) for x in output[y]]))