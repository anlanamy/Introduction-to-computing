#37 cAPS lOCK
l=input()
m=0
for i in range(len(l)-1):
    m+=l[i+1].isupper()
if m==len(l)-1 or len(l)==1:
    l=l.swapcase()
print(l)

#题目叙述不清楚，实际上全部大写的词需要全部变成小写orz。mark几个函数：capitalize()/title()/swapcase()