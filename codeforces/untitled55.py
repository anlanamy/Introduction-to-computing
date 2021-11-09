#56 Anton and Polyhedrons
n=int(input())
d={'Tetrahedron':4,'Cube':6,'Octahedron':8,'Dodecahedron':12,'Icosahedron':20}
s=0
for i in range(n):
    s+=d[input()]
print(s)
