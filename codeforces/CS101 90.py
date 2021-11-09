#CS101 90
r,c=map(int,input().split())
l=[[10001]*(c+2)]+[[10001]+[int(x) for x in input().split()]+[10001] for i in range(r)]+[[10001]*(c+2)]
output=[[0]*(c+2) for i in range(r+2)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dp(i,j):
    if output[i][j]>0:
        return output[i][j]
    for s in range(4):
        if l[i][j]>l[i+dx[s]][j+dy[s]]:
            output[i][j]=max(output[i][j],dp(i+dx[s],j+dy[s])+1)
    return output[i][j]

ans=0
for i in range(1,r+1):
    for j in range(1,c+1):
        ans=max(ans,dp(i,j))
print(ans+1)