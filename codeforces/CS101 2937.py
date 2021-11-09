#CS101 2937
N=int(input())
A=[[int(x) for x in input().split()] for i in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def abnormal(x,y):
    count=0
    for i in range(4):
        if A[x+dx[i]][y+dy[i]]>=A[x][y]+50:
            count+=1
        else:
            return False
    if count==4:
        return True

ans=0
for i in range(1,N-1):
    for j in range(1,N-1):
        if abnormal(i,j):
            ans+=1
print(ans)