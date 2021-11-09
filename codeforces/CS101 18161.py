#CS101 18161
rowA,colA=map(int,input().split())
A=[[int(x) for x in input().split()] for i in range(rowA)]
rowB,colB=map(int,input().split())
B=[[int(x) for x in input().split()] for i in range(rowB)]
rowC,colC=map(int,input().split())
C=[[int(x) for x in input().split()] for i in range(rowC)]
if colA!=rowB or rowA!=rowC or colB!=colC:
    print('Error!')
else:
    ans=[[0]*colB for i in range(rowA)]
    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                ans[i][j]+=A[i][k]*B[k][j]
            ans[i][j]+=C[i][j]
    for i in range(rowC):
        print(' '.join([str(x) for x in ans[i]]))