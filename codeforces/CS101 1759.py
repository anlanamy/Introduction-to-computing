#CS101 1759
n=int(input())
l=[int(x) for x in input().split()]
s=[1]*n
for i in range(1,n):
    for j in range(i):
        if l[i]>l[j]:
            s[i]=max(s[j]+1,s[i])
print(max(s))