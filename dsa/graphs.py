n = 8

A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

M = []
for i in range(n):
    M.append([0]*n)

for u,v in A:
    M[u][v] = 1

for i in M:
    print(i)

from collections import defaultdict

D = defaultdict(list)
for i,j in A:
    D[i].append(j)
print(D)

def dfs_recursive(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)
        # print(nei_node)
source = 0
seen = set()
seen.add(source)
dfs_recursive(source)

print(2 not in [1,2])
