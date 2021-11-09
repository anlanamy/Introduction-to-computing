#CS101 2810
N=int(input())
l=[0]*(N+2)
ans=[]
for i in range(N+1):
    l[i]=i**3
for a in range(6,N+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if l[a]==l[b]+l[c]+l[d]:
                    ans.append([a,b,c,d])
for i in range(len(ans)):
    print('Cube = ',ans[i][0],', Triple = (',ans[i][1],',',ans[i][2],',',ans[i][3],')',sep="")