#33 Beautiful Year
n=int(input())
while len(list(str(n+1)))!=len(set(list(str(n+1)))):
    n+=1
print(n+1)