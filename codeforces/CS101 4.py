#CS101 4
n=int(input())
l=[]
for i in range(n):
    l.append([int(x) for x in input().split()])
l.sort(key=lambda x:x[1])
s=0
if l[0][1]<=60:
    s=1
t2=l[0][1]
for i in range(n):
    if l[i][0]>t2:
        s+=1
        t2=l[i][1]
    if l[i][1]>60:
        break
print(s)