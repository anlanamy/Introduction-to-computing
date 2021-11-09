#CS101 16529
n=int(input())
l=[float(x) for x in input().split()]
m=[[l[0],l[n-1],0] for i in range(n)]
for i in range(n-1):
    m[i+1][0]=min(m[i][0],l[i+1])
    m[n-i-2][1]=max(m[n-i-1][1],l[n-i-2])
ans=1
for i in range(n):
    ans=max(ans,m[i][1]/m[i][0])
print('{:.2f}'.format(100*ans))