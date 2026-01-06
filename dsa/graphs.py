from collections import defaultdict
n  = 8
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

M = []

for i in range(n):
    M.append([0]*n)

# convert the input list into adjacency matrix
for u,v in A:
    M[u][v] = 1
    M[v][u] = 1

for row in M:
    print(*row)

# convert the input list into adjacency list

D = defaultdict(list)

for u,v in A:
    D[u].append(v)
    # D[v].append(u) # for undirected

# DFS

def dfs_recursive(node):
    print(node)

    for i in D[node]:
        if i not in seen:
            seen.add(i)
            dfs_recursive(i)


source = 0

seen = set()
seen.add(source)
dfs_recursive(source)