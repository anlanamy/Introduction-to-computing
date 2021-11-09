#number of ways
n=int(input())
l=[int(x) for x in input().split()]
m=0
s=0
k=sum(l)
if k%3!=0:
    print(0)
else:
    j=0
    for i in range(n-1):
        s+=l[i]
        if s==k//3:
            j+=1
        if s==(k//3)*2:
            m+=j
    print(m)