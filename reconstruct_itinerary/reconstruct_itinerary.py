from collections import defaultdict


class Solution:
    def findItinerary(self, graph):
        result = []
        paths = defaultdict(list)
        
        def dfs(dep):
            array = paths[dep]
            while array:
                dfs(array.pop())
            result.append(dep)

        graph.sort(key=lambda x: x[1], reverse=True)
        for s, t in graph:
            paths[s].append(t)
        dfs('JFK')
        
        return result[::-1]
