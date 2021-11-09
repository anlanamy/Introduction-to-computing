#CS101 2915
while True:
    try:
        n=int(input())
        l=[]
        for i in range(n):
            w=input()
            if w=='stop':
                break
            else:
               l.append(w)
        l.sort(key=lambda x:len(x))
        for i in l:
            print(i)
    except EOFError:
        break