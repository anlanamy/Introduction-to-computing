#CS101 1003 hangover
l=input()
while l!='0.00':
    n=float(l)
    count=0.5
    ans=1
    while count<n:
        ans+=1
        count+=1/(ans+1)
    print(ans,'card(s)')
    l=input()