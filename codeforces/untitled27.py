#28 translation
s=''.join(list(reversed(input())))
t=input()
print('YES' if s==t else 'NO')

#notice that the output of reverse function is not a string! it must be transformed into list first