#61 Vanya and Lanterns
n,l=map(int,input().split())
m=list(sorted({int(x) for x in input().split()}))
m2=max(m[0],l-m[-1])
for i in range(len(m)-1):
    m2=max(m2,(m[i+1]-m[i])/2)
print(m2)