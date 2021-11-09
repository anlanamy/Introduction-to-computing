#CS101 1289
n=int(input())
while n!=0:
    l1=[int(x) for x in input().split()]
    l1.sort(reverse=True)
    l2=[int(x) for x in input().split()]
    l2.sort(reverse=True)
    ans=0
    for _ in range(n):
        if l2[0]<l1[0]:
            ans+=1
            del l2[0]
            del l1[0]
        else:
            if l2[-1]<l1[-1]:
                ans+=1
                del l2[-1]
                del l1[-1]
            else:
                if l2[0]>l1[-1]:
                    ans-=1
                del l2[0]
                del l1[-1]
    print(200*ans)
    n=int(input())