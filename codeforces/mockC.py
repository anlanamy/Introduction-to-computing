#3
string=input().lower()
output=[]
count=1
for i in range(1,len(string)):
    if string[i]==string[i-1]:
        count+=1
    else:
        output.append([string[i-1],count])
        count=1
output.append([string[-1],count])

for i in range(len(output)):
    print('('+','.join([str(x) for x in output[i]])+')',end="")