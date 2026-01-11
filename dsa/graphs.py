from collections import defaultdict
n  = 7
A = [[1,2],[2,5],[1,3],[1,4],[3,4],[2,6],[6,5]]

M = []
# convert the input list into adjacency list

D = defaultdict(list)

for u,v in A:
    D[u].append(v)
    # D[v].append(u) # for undirected

# DFS
# print(D)
def dfs_recursive(node):
    print(node)

    for i in D[node]:
        if i not in seen:
            seen.add(i)

            dfs_recursive(i)
def is_in(node)->bool:
    if node in seen: return True
    return False


def insertion(val,neighbors):
    if is_in(val):
        print("The value is already in the graph")
        return None

    for i in neighbors:
        if i in D.keys(): 
            D[i].append(val)


source = 1

seen = set()
seen.add(source)

insertion(-1,[2,5])

print(D)

dfs_recursive(1)