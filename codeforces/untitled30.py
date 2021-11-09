#31 taxi
n=int(input())
l=input().split()
m=l.count('4')+l.count('3')+(l.count('2')+1)//2+((max(0,l.count('1')-l.count('3')-2*(l.count('2')%2))+3)//4)
print(m)
