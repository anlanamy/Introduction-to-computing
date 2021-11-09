#5 next round
n,m=map(int,input().split())
l=list(map(int,input().split()))
a=0
for i in range(n):
    if l[i]>=l[m-1] and l[i]>0:
        a+=1
print(a)

        