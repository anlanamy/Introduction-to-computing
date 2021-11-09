#The New Year: Meeting Friends
a,b,c=map(int,input().split())
print(abs(a-(a+b+c)//3)+abs(b-(a+b+c)//3)+abs(c-(a+b+c)//3))