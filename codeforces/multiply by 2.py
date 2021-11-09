#Multiply by 2, divide by 6
n=int(input())
for i in range(n):
    m=int(input())
    a=0
    b=0
    while m%3==0:
        m/=3
        a+=1
    while m%2==0:
        m/=2
        b+=1
    print(2*a-b if m==1 and a>=b else '-1')