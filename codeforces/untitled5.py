#6 string task
l=str(input())
l=l.lower()
l=l.replace('a','').replace('o','').replace('e','').replace('i','').replace('y','').replace('u','')
b=' '
l=b+l
l='.'.join(l)
print(l[1:])

str = input()
word = str.lower()
output = []
vowel = ['a','e','i','o','u','y'] 
for char in word:
    if char not in vowel: 
        output.append('.')
        output.append(char)
print(''.join(output))