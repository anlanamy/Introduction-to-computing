#1
a=int(input())
if a%2==0:
    if a%4==0:
        print(a//4,a//2)
    else:
        print((a+2)//4,a//2)
else:
    print('0 0')