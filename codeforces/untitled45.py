#46 puzzles
m,n=map(int,input().split())
l=sorted(map(int,input().split()))
s=l[m-1]-l[0]
for i in range(n-m+1):
    s=min(s,l[m+i-1]-l[i])
print(s)

#算法提醒：由于输入并不一定都是相异的，所以这里需要遍历！！