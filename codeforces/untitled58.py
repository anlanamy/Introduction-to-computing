#59 Amusing Joke
a=input()
b=input()
c=sorted(list(input()))
l=sorted(list(a+b))
print('YES' if c==l else 'NO')

#含有重复元素的列表进行比较，可以用sort函数解决！