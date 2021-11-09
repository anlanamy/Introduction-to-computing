#4
n=int(input())
l=[int(x) for x in input().split()]
li=[[0,0] for i in range(n)]
for i in range(n):
    li[i][0]=i+1
    li[i][1]=l[i]
li.sort(key=lambda x:x[1])
t=0
for i in range(n):
    t+=(n-1-i)*li[i][1]
for i in range(n-1):
    print(li[i][0],end=" ")
print(li[n-1][0],end="\n")
print('{:.2f}'.format(t/n))