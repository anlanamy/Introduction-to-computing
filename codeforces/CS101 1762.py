#CS101 1762
n=int(input())
l1=[int(x) for x in input().split()]
for i in range(n-1):
    l2=[int(x) for x in input().split()]
    l3=[l2[0]+l1[0]]+[max(l1[i],l1[i+1])+l2[i+1] for i in range(len(l2)-2)]+[l2[-1]+l1[-1]]
    l1=l3
print(max(l1))
