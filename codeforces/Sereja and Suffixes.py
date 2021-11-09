#Sereja and Suffixes
n,m=map(int,input().split())
l=[int(x) for x in input().split()]
l.reverse()
s={l[0]}
l2=[1]*n
for i in range(n-1):
    if l[i+1] not in s:
        s.add(l[i+1])
        l2[i+1]=l2[i]+1
    else:
        l2[i+1]=l2[i]
for i in range(m):
    print(l2[n-int(input())])