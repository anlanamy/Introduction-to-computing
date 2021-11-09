#CS101 19948
n,m=map(int,input().split())
l=sorted([int(x) for x in input().split()])
diff=[0]*(n-1)
for i in range(n-1):
    diff[i]=l[i+1]-l[i]
print(sum(sorted(diff,reverse=True)[m-1:]))