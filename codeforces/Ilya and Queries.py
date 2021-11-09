#Ilya and Queries
s=input()
n=len(s)
l1=[0]*n
for i in range(n-1):
    if s[i]==s[i+1]:
        l1[i+1]+=1
for i in range(n-2):
    l1[i+2]+=l1[i+1]
m=int(input())
for i in range(m):
    l,r=map(int,input().split())
    print(l1[r-1]-l1[l-1])