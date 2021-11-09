#CS101 18182
cases=int(input())
for i in range(cases):
    n,m,b=map(int,input().split())
    l=[]
    for j in range(n):
        l.append([int(x) for x in input().split()])
    l.sort(key=lambda x:(x[0],-x[1]))
    k=1
    b-=l[0][1]
    for j in range(1,n):
        if b<=0:
            break
        if l[j][0]==l[j-1][0]:
            k+=1
        else:
            k=1
        if k<=m:
            b-=l[j][1]
        if j==n-1 and b<=0:
            j+=1
    print(l[j-1][0] if b<=0 else 'alive')