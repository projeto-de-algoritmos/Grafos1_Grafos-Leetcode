#!/usr/bin/env python3
from collections import Counter


def is_ring(edges: list[int]) -> bool:
    # a graph is a ring if all nodes have 2 edges
    return all(e == 2 for e in edges)


def is_bus(edges: list[int], n: int) -> bool:
    # a graph is a bus if 2 nodes have 1 edge and all remaining have 2 edges
    c = Counter(edges)
    return c[1] == 2 and c[2] == n - 2


def is_star(edges: list[int], n: int) -> bool:
    # a graph is a star if one node has (n-1) edges and
    # all remaining have 1 edge each
    c = Counter(edges)
    return c[n-1] == 1 and c[1] == n-1


def solve():
    n, m = map(int, input().split())

    edge_count = [0] * n

    for _ in range(m):
        u, v = map(int, input().split())
        edge_count[u-1] += 1
        edge_count[v-1] += 1

    if is_ring(edge_count):
        print("ring topology")
    elif is_bus(edge_count, n):
        print("bus topology")
    elif is_star(edge_count, n):
        print("star topology")
    else:
        print("unknown topology")

solve()
