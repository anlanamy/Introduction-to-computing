#CS101 18155
T=int(input())
l=[int(x) for x in input().split()]
copyl=l[:]
for i in copyl:
    if T%i!=0 or i==1:
        l.remove(i)
ans=set()
for i in l:
    ans.add(i)
    copyans=list(ans)
    for j in copyans:
        ans.add(i*j)
print('YES' if T in ans else 'NO')