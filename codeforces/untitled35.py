#36 Kefa and First Steps
n=int(input())
l=list(map(int,input().split()))
m=j=1
for i in range(n-1):
    if l[i+1]>=l[i]:
        j+=1
        m=max(j,m)
    else:
        j=1
print(m)

#notice that range must be n-1; it helps shorten time by using max function