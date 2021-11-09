# 2048 game
n=int(input())
for i in range(n):
    s=0
    m=int(input())
    l=list(map(int,input().split()))
    for j in l:
        if j<=2048:
            s+=j
    print('YES' if s>=2048 else 'NO')