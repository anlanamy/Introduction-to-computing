#3 Way Too Long Words
n=int(input())
for i in range(n):
    word=input()
    length=len(word)
    print(word[0]+str(length-2)+word[-1] if length>10 else word)
#    if length>10:
#       print(word[0]+str(length-2)+word[-1])
#    else:
#       print(word)

