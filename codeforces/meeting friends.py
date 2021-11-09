#The New Year: Meeting Friends
a,b,c=sorted(map(int,(input().split())))
m=b+c-2*a
for i in range(a,c+1):
    m=min(m,abs(a-i)+abs(b-i)+abs(c-i))
print(m)