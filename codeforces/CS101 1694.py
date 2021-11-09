#CS101 1694
def balance(l1,l2,l3):
    s1=s2=0
    for i in l1:
        s1+=d[i]
    for i in l2:
        s2+=d[i]
    if (s1>s2 and l3=='up') or (s1<s2 and l3=='down') or (s1==s2 and l3=='even'):
        return True
    else:
        return False
               
n=int(input())
for i in range(n):
    l=[input().split() for i in range(3)]
    d={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0}
    status=[-1,1]
    word=['light.','heavy.']
    for j in range(24):
        d[list(d.keys())[j//2]]=status[j%2]
        for k in range(3):
            if balance(l[k][0],l[k][1],l[k][2])==False:
                break
            if k==2 and balance(l[k][0],l[k][1],l[k][2])==True:
                ans=j
        d={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0}
    print(list(d.keys())[ans//2]+' is the counterfeit coin and it is '+word[ans%2])