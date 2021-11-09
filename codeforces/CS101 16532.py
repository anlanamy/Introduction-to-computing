#CS101 16532
hole=[[0,0],[8,0],[16,0],[0,5],[8,5],[16,5]]
wx,wy=map(int,input().split())
bx,by=map(int,input().split())
tx,ty=map(int,input().split())
e=int(input())
sign=0
output=0
while e>0:
    e-=1
    if wx==bx and wy==by:
        sign=1
    wx+=tx
    wy+=ty
    if wx==0 or wx==16:
        tx=-tx
    if wy==0 or wy==5:
        ty=-ty
    for i in range(6):
        if wx==hole[i][0] and wy==hole[i][1]:
            if sign==0:
                output=-1
            else:
                output=1
            break
print(output)