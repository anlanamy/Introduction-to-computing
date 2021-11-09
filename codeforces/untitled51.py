#52 Arrival of the General
n=int(input())
l=[int(x) for x in input().split()]
a=l[0]
b=l[-1]
c=d=0
for i in range(n):
    if l[i]>a:
        c=i
        a=l[i]
    if l[n-1-i]<b:
        d=i
        b=l[n-1-i]
print(c+d if c+d<n else c+d-1)
    
    