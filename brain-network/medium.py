from collections import defaultdict, deque


def get_distances(root: int, connectors: dict[int, list[int]]) -> list[tuple[int, int]]:
    visited = set([root])
    g = set([root])

    # the first level is already one node away
    i = 1

    # the distances are stored as a list of tuples,
    # where the first element of the tuple is the node
    # in question and the second one is the distance
    # to the root
    distances = []

    while True:
        # get only the nodes that are i nodes away from the root
        g = {k for j in g for k in connectors[j] if k not in visited}

        if not g:
            # if there are no nodes at this level,
            # we've already visited all of them.
            return distances

        # marking the current nodes as visited,
        # so we dont go through them multiple times.
        visited |= g

        # adding the nodes to the distance list
        distances.extend((k, i) for k in g)

        i += 1


def solve():
    _, m = map(int, input().split())
    connectors = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        connectors[u].append(v)
        connectors[v].append(u)

    distances_from_root = get_distances(1, connectors)

    # we can use the second tuple element, which is the distance,
    # as the key for the `max` function to get the furthest brain
    furthest_brain, _ = (
        max(distances_from_root, key=lambda x: x[1]))

    # ignore the first variable, since we only need the distance here
    #
    # the same technique as above is used, but to get the distance this time.
    _, max_distance_from_furthest_brain = max(
        get_distances(furthest_brain, connectors), key=lambda x: x[1])

    print(max_distance_from_furthest_brain)


solve()
