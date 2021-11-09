#CS101 18106
n=int(input())
l=[[-1]*(n+2)]+[[-1]+[0]*n+[-1] for j in range(n)]+[[-1]*(n+2)]
turn=[[0,1],[1,0],[0,-1],[-1,0]]
i=1
j=1
s=1
t=0
while s<=n**2:
    l[i][j]=s
    s+=1
    if l[i+turn[t][0]][j+turn[t][1]]!=0:
        t=(t+1)%4
    i+=turn[t][0]
    j+=turn[t][1]
for i in range(1,n+1):
    print(' '.join([str(x) for x in l[i][1:n+1]]))
