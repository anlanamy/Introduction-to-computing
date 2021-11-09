#38 magnets
n=int(input())
m=1
j=input()
for i in range(n-1):
    k=input()
    if j!=k:
        m+=1
    j=k
print(m)
    