#1
n=int(input())
while n!=1:
    if n%2==0:
        print("{}/2={}".format(n,n//2))
        n=n//2
    else:
        print("{}*3+1={}".format(n, n*3+1))
        n=n*3+1