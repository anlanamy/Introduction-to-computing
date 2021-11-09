#57 Games
n=int(input())
l=[]
s=0
for i in range(n):
    l.append(input().split())

for j in range(n):
    for k in range(n):
        if l[j][1]==l[k][0]:
            s+=1
print(s)