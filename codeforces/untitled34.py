#35 Vanya and Fence
n,h=map(int,input().split())
l=list(map(int,input().split()))
m=0
for i in l:
    if i<=h:
        m+=1
    else:
        m+=2
print(m)