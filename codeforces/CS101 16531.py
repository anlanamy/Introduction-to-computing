#CS101 16531
def same(l,board,x,y):
    if l[board[x][y]]==l[board[x-1][y]] or l[board[x][y]]==l[board[x][y-1]] or l[board[x][y]]==l[board[x][y+1]] \
    or l[board[x][y]]==l[board[x+1][y]]:
        return 1
    else:
        return 0
m,n=map(int,input().split())
board=[[-1]*(n+2)]+[[-1]+[int(x) for x in input().split()]+[-1] for j in range(m)]+[[-1]*(n+2)]
l=[]
score=[]
for i in range(m*n):
    l1=[int(x) for x in input().split()]
    l.append(l1)
    score.append(sum(l1))
l.append([])
s=0
for i in range(m):
    for j in range(n):
        s+=same(l,board,i+1,j+1)
score.sort(reverse=True)
t=0
for i in range(m*n*2//5):
    if score[i]>score[m*n*2//5]:
        t+=1
print(s,t,sep=' ')