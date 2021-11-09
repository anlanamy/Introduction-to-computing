#CS101 16528dp
n=int(input())
l=[-1 for i in range(61)]
for i in range(n):
    a,b=map(int,input().split())
    if l[b]<a:
        l[b]=a
s=0
m=-1
for i in range(61):
    if l[i]>m:
        s+=1
        m=i
print(s)