#2
m=int(input())              
for i in range(m):
    l=[int(x) for x in input().split()]
    j=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    s=l[0]*(2*(a%2)-1)+l[1]*(2*(b%2)-1)+l[2]*(2*(c%2)-1)+l[3]*(2*(d%2)-1)
                    if s==24:
                        j=1
    print('YES' if j==1 else 'NO')