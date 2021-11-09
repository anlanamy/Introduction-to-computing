#CS101 2
n=int(input())
s=0
for i in range(n):
    l=input()
    l1=l.replace('### ###',' ')
    s+=l1.count('###')//2
print(s)