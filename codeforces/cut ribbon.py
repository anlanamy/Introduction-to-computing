#cut ribbon
def dpcut(lengthlist,l,maxcuts):
    for i in range(l+1):
        for j in [c for c in lengthlist if c<=i]:
            if maxcuts[i-j]+1>maxcuts[i]:
                maxcuts[i]=maxcuts[i-j]+1
    return maxcuts[l]       
l,a,b,c=map(int,input().split())
lengthlist=list({a,b,c})
maxcuts=[0]+[-1000000]*(l)
print(dpcut(lengthlist,l,maxcuts))