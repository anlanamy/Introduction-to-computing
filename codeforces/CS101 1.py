#CS101 1
n=int(input())
dic={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
for i in range(n):
    l=input()
    year=int(l[0:4])+(int(l[4:6])-3)//12
    c=int(str(year)[:2])
    y=int(str(year)[2:])
    m=int(l[4:6])-12*((int(l[4:6])-3)//12)
    d=int(l[6:8])
    print(dic[(y+y//4+c//4-2*c+(26*(m+1))//10+d-1)%7])