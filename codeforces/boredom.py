#Boredom
n=int(input())
l1=[int(x) for x in input().split()]
l2=[0]*(max(l1)+1)
for i in l1:
    l2[i]+=1
f=[0]*(max(l1)+1)
for i in range(max(l1)+1):
    f[i]=max(f[i-1],f[i-2]+i*l2[i])
print(f[max(l1)])