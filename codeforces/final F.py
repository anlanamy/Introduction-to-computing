#6
T,n=map(int,input().split())
dp=[-1]*(T+1)
copydp=dp[:]
for i in range(n):
    x,y=map(int,input().split())
    dp[x]=max(copydp[x],y)
    for j in range(x+1,T+1):
        if copydp[j-x]>=0:
            dp[j]=max(copydp[j],copydp[j-x]+y)
    copydp=dp[:]
print(dp[T])