#34 presents
n=int(input())
l=input().split()
output=[]
for i in range(n):
    output.append(str(l.index(str(i+1))+1))
print(' '.join(output))
