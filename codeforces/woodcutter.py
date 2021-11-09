#woodcutter
n=int(input())
if n==1 or n==2:
    print(n)
else:
    l=[]
    for i in range(n):
        l.append([int(x) for x in input().split()])
        s=2
    for i in range(n-2):
        if l[i+1][0]-l[i][0]>l[i+1][1]:
            s+=1
        else:
            if l[i+2][0]-l[i+1][0]>l[i+1][1]:
                s+=1
                l[i+1][0]+=l[i+1][1]
    print(s)
