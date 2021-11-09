#CS101 3532
n=int(input())
l=[int(x) for x in input().split()]
s=l[:]
for i in range(1,n):
    for j in range(i):
        if l[i]>l[j]:
            s[i]=max(s[j]+l[i],s[i])
print(max(s))