#IQ test
input()
l=[int(x) for x in input().split()]
s=0
for i in l:
    if i%2==0:
        s+=1
if s>len(l)//2:
    for i in l:
        if i%2==1:
            print(l.index(i)+1)
            break
else:
    for i in l:
        if i%2==0:
            print(l.index(i)+1)
            break
        
