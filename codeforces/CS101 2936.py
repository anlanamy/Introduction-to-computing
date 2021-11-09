#CS101 2936
N=int(input())
l={int(x) for x in input().split()}
ans=0
if 7 in l or 8 in l:
    if {1,2}.issubset(l)==False:
        if {3,4}.issubset(l)==False:
            if {5,6}.issubset(l)==True or {5,6}&l==set():
                ans=1
                
print(ans)