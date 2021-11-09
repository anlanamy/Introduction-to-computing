#31 George and Accommodation
n=int(input())
m=0
for i in range(n):
    a,b=map(int,input().split())
    if b-a>=2:
        m+=1
print(m)
        