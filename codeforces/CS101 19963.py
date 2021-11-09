#CS101 19963
n=int(input())
l=input()
price=[int(x) for x in input().split()]
l1=l[1:len(l)-2].split(') (')
l2=[[0,0] for i in range(n)]
distance=[0]*n
ratio=[0]*n
for i in range(n):
    l2[i][0],l2[i][1]=map(int,l1[i].split(','))
    distance[i]=l2[i][0]+l2[i][1]
    ratio[i]=distance[i]/price[i]
if n%2==0:
    ratiom=(sorted(ratio)[n//2]+sorted(ratio)[n//2-1])/2
    pricem=(sorted(price)[n//2]+sorted(price)[n//2-1])/2
else:
    ratiom=sorted(ratio)[n//2]
    pricem=sorted(price)[n//2]
ans=0
for i in range(n):
    if price[i]<pricem and ratio[i]>ratiom:
        ans+=1
print(ans)