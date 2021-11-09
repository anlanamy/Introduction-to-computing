#light it up
n,m=map(int,input().split())
l=[int(x) for x in input().split()]
j=0
b=[0]*(n+1)
b[0]=l[0]
for i in range(0,n-1):
    b[i+1]=b[i]+(-1+2*(i%2))*(l[i+1]-l[i])
b[-1]=b[n-1]+(1-2*(n%2))*(m-l[-1])
print(max((b[-1]+m)//2,(m+2*max(b)-b[-1]-1)//2))