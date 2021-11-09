#50 I Wanna Be the Guy
n=int(input())
l1=list(map(int,input().split()))[1:]
l2=list(map(int,input().split()))[1:]
s=set(l1+l2)
if s==set(range(1,n+1)):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')