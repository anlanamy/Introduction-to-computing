#CS101 1756
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
n=int(input())
for i in range(n):
    print(''.join([str(x+1) for x in l[int(input())-1]]))