#!/usr/bin/env python3
from collections import defaultdict

def dfs(brain: int, connectors: dict[int, list[int]], visited: set[int] = None) -> set[int]:
    """Simple recursive depth-first search."""

    # visited cannot have a set() as a default parameter,
    # since objects get reused between multiple function
    # invocations.
    #
    # using None as a "sentinel" value is a common technique
    # to avoid this behavior.
    if visited is None:
        visited = set()

    if brain in visited:
        return

    visited.add(brain)

    # recurse the graph to do a search in every node
    # connected to the current one
    for b in connectors[brain]:
        dfs(b, connectors, visited)

    return visited


def solve():
    n, m = map(int, input().split())

    # one of the conditions is that the number
    # of edges is equal to the number of brains
    # minus 1
    if m != n - 1:
        print("no")
        return

    connectors = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        connectors[u].append(v)
        connectors[v].append(u)

    visited = dfs(1, connectors)

    # if the graph is connected, visited should be equal to
    # the set of numbers between 1 and n, inclusive.
    if visited == set(range(1, n + 1)):
        print("yes")
    else:
        print("no")


solve()
