#24 twins
n=int(input())
l=sorted(map(int,input().split()))
m=0
for i in range(n):
    m=m+l[i]
j=1
s=0
while s<=m/2:
    s+=l[-j]
    j+=1
print(j-1)

#debug心得：字符串排序是按照第一个字符来排序，所以在这种情况下11<2，
#不满足数的排序，所以仍然需要在第一步用map函数把列表中的数据都改成整数#
#[~i]表示倒序遍历，仍然从0开始