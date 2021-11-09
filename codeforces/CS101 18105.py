#CS101 18105
l=sorted([int(x) for x in input().split()])
num=[0]*(l[-1]+1)
ans=0
for i in l:
    for j in range(i+1):
        num[j]+=1
for h in range(l[-1]+1):
    if num[h]>=h:
        ans=h
print(ans)