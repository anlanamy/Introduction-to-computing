#20 tram
n=int(input())
m=0
maxium=0
for i in range(n):
    a,b=map(int,input().split())
    m=m-a+b
    if m>maxium:
        maxium = m
print(maxium)