#CS101 18104
g=sorted([int(x) for x in input().split()])
s=sorted([int(x) for x in input().split()])
ans=0
t=0
i=0
while t<len(g):
    if g[t]<=s[i]:
        ans+=1
        t+=1
        i+=1
    else:
        i+=1
    if i>=len(s):
        break
print(ans)