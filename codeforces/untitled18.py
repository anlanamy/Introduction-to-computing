#19 chat room
l=input()
o=-1
if l.find('h')!=-1:
    h=l.find('h')
    if l[h+1:].find('e')!=-1:
        e=l[h+1:].find('e')
        if l[h+e+2:].find('l')!=-1:
            ll=l[h+e+2:].find('l')
            if l[h+e+ll+3:].find('l')!=-1:
                lll=l[h+e+ll+3:].find('l')
                if l[h+e+ll+lll+4:].find('o')!=-1:
                    o=l[h+e+ll+lll+4:].find('o')
print('YES' if o>-1 else 'NO')

#####debug心得：还是没有排除每一种可能，需要一步一步老老实实走循环