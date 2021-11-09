#CS101 2943
N=int(input())
l=[]
for i in range(N):
    w,c=input().split()
    w=int(w)
    l.append([w,c])
l.sort(key=lambda x:-x[0])
for i in range(N):
    print(l[i][1])