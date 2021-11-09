#55 Divisibility Problem
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(0 if a%b==0 else b-a%b)
    
#if the time exceeds, try to form a math formula instead of rolling