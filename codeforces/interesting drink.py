#Interesting drink
n=int(input())
l=[int(x) for x in input().split()]
maxl=max(l)
l2=[0]*(maxl+1)
for i in l:
    l2[i]+=1
for j in range(2,maxl+1):
    l2[j]+=l2[j-1]
q=int(input())
output=[]
for i in range(q):
    m=int(input())
    if m>=maxl:
        output.append(str(n))
    else:
        output.append(str(l2[m]))
print('\n'.join(output))