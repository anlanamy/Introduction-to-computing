#5
n,w=map(int,input().split())
P,Q=map(int,input().split())
M=P+Q
l=[]
ans=0
for i in range(n):
    xi,yi=map(int,input().split())
    if M>=xi:
        l.append(yi)
l.sort()
for i in range(len(l)):
    if w>=l[i]:
        w-=l[i]
        ans+=1
    else:
        break
print(ans)