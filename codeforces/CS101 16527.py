#CS101 16527
l1=input()
l2=input()
m=min(len(l2),len(l1))
ans=0
for i in range(m):
    if l1[len(l1)-i-1:]==l2[:i+1]:
        ans=i
        break
print(len(l1)-1-ans)