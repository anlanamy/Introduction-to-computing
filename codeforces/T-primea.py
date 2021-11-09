#T-primes        
l=[True]*1000001
l[0]=l[1]=False
for i in range(1001):
    if l[i]==True:
        for j in range(2*i,1000001,i):
            l[j]=False
n=int(input())
k=[int(x) for x in input().split()]
for i in range(n):
    if k[i]**0.5!=int(k[i]**0.5):
        print('NO')
    else:
        print('YES' if l[int(k[i]**0.5)]==True else 'NO')