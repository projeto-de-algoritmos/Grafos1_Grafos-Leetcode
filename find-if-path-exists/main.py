#!/usr/bin/env python3
from collections import defaultdict, deque


class Solution:
    """
    Solution for 1971. Find if Path Exists in Graph
    https://leetcode.com/problems/find-if-path-exists-in-graph/
    """
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        """
        This function does a BFS (Breadth-First Search)
        to find if there is a path between a source and destination.
        """

        # g represents the graph
        # it is a dict of lists, where the key is the node and the
        # value is a list of adjacent nodes
        g = defaultdict(list)

        # building the graph by iterating over the edges and inserting
        # them into the graph
        for (u, v) in edges:
            # we can safely append here since the problem description
            # guarantees that there will be no duplicates.
            g[u].append(v)
            g[v].append(u)


        # the set of visited nodes
        visited = set()

        queue = deque()

        queue.appendleft(source)
        visited.add(source)

        while len(queue):
            current = queue.pop()

            if current == destination:
                return True

            # adding all adjacent nodes if they haven't been visited yet.
            queue.extendleft(x for x in g[current] if x not in visited)

            # since the adjacent nodes are already in the queue,
            # we can set them as visited right now
            visited |= set(g[current])


        # if the loop exits, this means that there
        # is no path between source and destination
        return False


# Basic test cases
# Don't include this in the LeetCode submission
assert Solution().validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True
assert Solution().validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) is False
assert (
    Solution().validPath(
        10,
        [
            [4, 3],
            [1, 4],
            [4, 8],
            [1, 7],
            [6, 4],
            [4, 2],
            [7, 4],
            [4, 0],
            [0, 9],
            [5, 4],
        ],
        5,
        9,
    )
    is True
)
