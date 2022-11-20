from collections import defaultdict

def dfs(root: int, edges: dict[int, list[int]], visited: set[int]=None):
    if visited is None:
        visited = set()

    if root in visited:
        return

    visited.add(root)    

    for node in edges[root]:
        dfs(node, edges, visited)

    return visited

def solve():
    n, m = map(int, input().split())

    # to be cthtulhu, the number of edges must be equal to the
    # number of nodes
    if n != m:
        print("NO")
        return

    edges = defaultdict(list) 

    for _ in range(m):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    visited = dfs(1, edges)

    # if all nodes have been visited, the graph is cthtulhu
    if visited == set(range(1, n + 1)):
        print("FHTAGN!")
    else:
        print("NO")

solve()
