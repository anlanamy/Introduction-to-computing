#8 bit++
n=int(input())
x=0
for i in range(n):
    s=input()
    if '++' in s:
        x=x+1
    else:
        x=x-1
print(x)