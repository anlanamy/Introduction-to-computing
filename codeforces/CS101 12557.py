#CS101 12557
l1=[int(x) for x in input().split('.')]
l2=[int(x) for x in input().split('.')]
for i in range(len(l1)):
    if l1[i]!=l2[i]:
        if l1[i]>l2[i]:
            print('.'.join([str(x) for x in l1]))
        else:
            print('.'.join([str(x) for x in l2]))
        break