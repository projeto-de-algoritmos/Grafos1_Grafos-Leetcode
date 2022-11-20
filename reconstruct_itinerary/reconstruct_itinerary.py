import collections


class Solution(object):
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        origin = "JFK"
        result = [origin]
        
        def route_helper(origin, graph, result, count_tickets):
            if count_tickets == 0:
                return True

            for i, (destiny, valid)  in enumerate(graph[origin]):
                if valid:
                    graph[origin][i][1] = False
                    result.append(destiny)
                    if route_helper(destiny, graph, result, count_tickets - 1):
                        return result
                    result.pop()
                    graph[origin][i][1] = True
            return False

        for k in graph.keys():
            graph[k].sort()
        for ticket in tickets:
            graph[ticket[0]].append([ticket[1], True])
        
        route_helper(origin, graph, result, len(tickets))
        return result
