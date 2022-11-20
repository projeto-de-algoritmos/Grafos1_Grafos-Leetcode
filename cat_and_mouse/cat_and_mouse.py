from collections import defaultdict, deque


class Solution:
    def catMouseGame(self, graph):
        def getPreStates(m, c, t):
            ans = []
            if t == 1:
                for c2 in graph[c]:
                    if c2 == 0:
                        continue
                    ans.append((m, c2, 2))
            else:
                for m2 in graph[m]:
                    ans.append((m2, c, 1))

            return ans

        def ifAllNextMovesFailed(m, c, t):
            if t == 1:
                for m2 in graph[m]:
                    if results[(m2, c, 2)] != 2:
                        return False
            else:
                for c2 in graph[c]:
                    if c2 == 0:
                        continue
                    if results[(m, c2, 1)] != 1:
                        return False

            return True

        results = defaultdict(int)
        n = len(graph)
        queue = deque()

        for t in range(1, 3):
            for i in range(1, n):
                results[(0, i, t)] = 1
                queue.append((0, i, t))

                results[(i, i, t)] = 2
                queue.append((i, i, t))

        while queue:
            m, c, t = queue.popleft()
            r = results[(m, c, t)]

            for m2,c2,t2 in getPreStates(m, c, t):
                r2 = results[(m2, c2, t2)]
                if r2 > 0:
                    continue

                if r == 3 - t:
                    results[(m2, c2, t2)] = r
                    queue.append((m2, c2, t2))
                elif ifAllNextMovesFailed(m2, c2, t2):
                    results[(m2, c2, t2)] = 3 - t2
                    queue.append((m2, c2, t2))

        return results[(1, 2, 1)]