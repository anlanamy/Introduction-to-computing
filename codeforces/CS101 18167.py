#CS101 18167
n=int(input())
for i in range(n):
    l=input()
    m=len(l)
    ans=0
    for j in range(1,m+1):
        sign=1
        if m%j==0:
            num=m//j
            for k in range(num):
                if l[:j]==l[k*j:(k+1)*j]:
                    sign=2
                    continue
                else:
                    sign=0
                    break
        if sign==2:
            print(j)
            break
        else:
            continue