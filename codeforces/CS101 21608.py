#CS101 21608
def dfs(graph,node,visited):
    if node!=-1 and node not in visited:
        visited.append(node)
        if node not in graph:
            return visited
        for nei in graph[node]:
            dfs(graph,nei,visited)
    return visited

graph={}
ids=set()
n=int(input())
for i in range(n):
    l=input().split(' : ')
    ids.add(int(l[0]))
    if int(l[0]) not in graph:
        graph[int(l[0])]=[int(x) for x in l[1].split()]

maxp=0
for i in ids:
    dfs_path=dfs(graph,i,[])
    maxp=max(maxp,len(dfs_path))
print(maxp)