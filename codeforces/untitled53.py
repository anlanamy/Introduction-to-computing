#54 Anton and Letters
l=input()[1:-1].split(', ')
print(len(set(l)) if '' not in set(l) else 0)