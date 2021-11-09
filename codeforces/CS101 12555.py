#CS101 12555
n=int(input())
l=sorted([float(x) for x in input().split()])
if n==1:
    for _ in range(3):
        print('{:.2f}'.format(l[0]))

else:
    for p in [1/4,1/2,3/4]:
        h=(n-1)*p+1
        print('{:.2f}'.format(l[int(h)-1]+(h-int(h))*(l[int(h)]-l[int(h)-1])))