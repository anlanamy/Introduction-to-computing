#CS101 18211
p=int(input())
l=[int(x) for x in input().split()]
l.sort()
j=1
n=len(l)
s=0
for i in range(n):
    if i+j>n:
        break
    else:
        if p>=l[i]:
            s+=1
            p-=l[i]
        else:
            p+=l[-j]
            s-=1
            if s<0:
                s=0
                break
            else:
                p-=l[i]
                j+=1
                s+=1
print(s)