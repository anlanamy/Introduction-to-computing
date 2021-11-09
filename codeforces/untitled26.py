#27 Word
l=input()
upper=lower=0
for i in l:
    upper+=i.isupper()
    lower+=i.islower()
print(l.upper() if upper>lower else l.lower())

#another way, notice that strings can be compared: if i>='A' and i<='Z'