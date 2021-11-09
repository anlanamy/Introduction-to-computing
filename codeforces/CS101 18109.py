#CS101 18109
l=input().lower()
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1 
d_key = max(d, key=lambda k: d[k]) 
print(d_key,d[d_key])