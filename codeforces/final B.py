#2
m=int(input())
ans=1
for i in range(6,m):
    if m%i==0:
        ans=m//i
        break
print(ans)