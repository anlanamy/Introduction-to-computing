#CS101 18224 找魔数
l=[0]*1001
for i in range(1,32):
    for j in range(1,32):
        if i**2+j**2<=1000:
            l[i**2+j**2]=1
        
m=int(input())
l1=[int(x) for x in input().split()]
for i in l1:
    if l[i]==1:
        print(bin(int(str(i),10)),oct(int(str(i),10)),hex(int(str(i),10)))
    else:
        continue