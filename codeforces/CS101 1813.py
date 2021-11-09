#CS101 1813
import copy
dx=[0,0,0,-1,1]
dy=[0,1,-1,0,0]
mat=[[2]*(8)]+[[2]+[int(x) for x in input().split()]+[2] for i in range(5)]+[[2]*(8)]
output=[[0]*(6) for i in range(5)]

def turn(x,y,k):
    if k==1:
        for i in range(5):
            if board[x+dx[i]][y+dy[i]]==0:
                board[x+dx[i]][y+dy[i]]=1
            elif board[x+dx[i]][y+dy[i]]==1:
                board[x+dx[i]][y+dy[i]]=0
        return
    if k==0:
        return

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        board=copy.deepcopy(mat)
                        output[0]=[a,b,c,d,e,f]
                        for i in range(6):
                            turn(1,i+1,output[0][i])
                        for i in range(2,6):
                            for j in range(1,7):
                                if board[i-1][j]==0:
                                    output[i-1][j-1]=0
                                else:
                                    output[i-1][j-1]=1
                                    turn(i,j,1)
                        if sum(board[5][1:7])==0:
                            for i in range(5):
                                print(' '.join([str(x) for x in output[i]]))