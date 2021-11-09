#58 Pangram
n=int(input())
l=input().lower()
s=[]
for i in range(n):
    s.append(l[i])
print('YES' if len(set(s))==26 else 'NO')