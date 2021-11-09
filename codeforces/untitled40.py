#41 even odds
n,k=map(int,input().split())
if n%2==0:
    if k>n//2:
        s=(k-n//2)*2
    else:
        s=2*k-1
else:
    if k>n//2+1:
        s=(k-n//2-1)*2
    else:
        s=2*k-1
print(s)