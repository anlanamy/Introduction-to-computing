#CS101 3
l=input()
while l!='0 0 0 0 0 0':
    a,b,c,d,e,f=map(int,l.split())
    d1={0:0,1:5,2:3,3:1}
    s=d+e+f-(-c)//4
    b1=max(0,b-5*d-d1[c%4])
    s=s-(-b1)//9-min((-4*b-9*c-16*d-25*e-36*f+36*(s-(-b1)//9)-a),0)//36
    print(s)
    l=input()