#CS101 1700
def queen(A,cur=0):
    if cur==len(A):
        l.append(A[:])
        return 0
    for i in range(len(A)):
        A[cur],flag=i,True
        for j in range(cur):
            if A[j]==A[cur] or abs(A[j]-A[cur])==cur-j:
                flag=False
                break
        if flag:
            queen(A,cur+1)
l=[]
queen([None]*8)
for i in range(92):
    print('No.',i+1)
    m=[[0]*8 for i in range(8)]
    for j in range(8):
        m[l[i][j]][j]=1
    for j in range(8):
        print(' '.join([str(x) for x in m[j][1,n+1]]))
        