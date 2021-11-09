#16 young physicist
n=int(input())
X=0
Y=0
Z=0
for i in range(n):
    x,y,z=map(int,input().split())
    X+=x
    Y+=y
    Z+=z
print('YES' if X==0 and Y==0 and Z==0 else 'NO')
    