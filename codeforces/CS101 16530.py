#CS101 16530
n=int(input())
l=[]
for i in range(n):
    l.append(input())
l.sort()
output=[]
if len(l[n//2])<len(l[n//2-1]):
    l[n//2]=l[n//2]+' '*(len(l[n//2-1])-len(l[n//2]))
for i in range(len(l[n//2-1])):
    if l[n//2-1][i]==l[n//2][i]:
        output.append(l[n//2-1][i])
    else:
        if i==len(l[n//2])-1:
            output.append(chr(ord(l[n//2-1][i])))
            break
        else:
            if l[n//2-1][i]=='Z' or (l[n//2][i+1]==' ' and ord(l[n//2-1][i])+1==ord(l[n//2][i])):
                output.append(l[n//2-1][i])
            else:
                output.append(chr(ord(l[n//2-1][i])+1))
                break
print(''.join(output))