#CS101 18164
N=int(input())
l=sorted([int(x) for x in input().split()])
ans=0
for i in range(N-1):
    remain=l[0]+l[1]
    ans+=remain
    l.remove(l[0])
    l.remove(l[0])
    l.append(remain)
    l.sort()
print(ans)