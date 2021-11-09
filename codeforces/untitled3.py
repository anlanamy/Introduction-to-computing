#4.Team
m=0
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a+b+c>1:
        s=1
    else:
        s=0
    m=m+s
print(m)