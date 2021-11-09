#the delivery dilemma
n=int(input())
output=[]
for i in range(n):
    m=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    l=[([0]*2) for i in range(m)]
    for j in range(m):
        l[j][0]=a[j]
        l[j][1]=b[j]
    l.sort(key=lambda x:x[0],reverse=True)
    t=l[0][0]
    s=0
    for j in range(m-1):
        s+=l[j][1]
        t=min(t,max(s,l[j+1][0]))
    output.append(str(min(t,s+l[m-1][1])))
print('\n'.join(output))