#45 Ultra-Fast Mathematician
n=input()
m=input()
l=[]
for i in range(len(n)):
    if n[i]==m[i]:
        l.append('0')
    else:
        l.append('1')
print(''.join(l))