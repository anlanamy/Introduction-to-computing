#CS101 7813
n,w=map(int,input().split())
l=[[int(x) for x in input().split()] for i in range(n)]
l.sort(key=lambda x: -x[0]/x[1])
ans=0
for i in range(n):
    if w>l[i][1]:
        ans+=l[i][0]
        w-=l[i][1]
    else:
        ans+=w*(l[i][0]/l[i][1])
        break
print('%.1f' % ans)