#3
n=int(input())
A=[[-1]*(n+2)]+[[-1]+[int(x) for x in input().split()]+[-1] for j in range(n)]+[[-1]*(n+2)]
turn=[[1,0],[0,1],[-1,0],[0,-1]]
s=1
ans=[]
i=1
j=1
t=0
while s<=n**2:
    if A[i][j]==0:
        break
    else:
        ans.append(chr(A[i][j]))
    s+=1
    A[i][j]=-1
    if A[i+turn[t][0]][j+turn[t][1]]==-1:
        t=(t+1)%4
    i+=turn[t][0]
    j+=turn[t][1]
print(''.join(ans))