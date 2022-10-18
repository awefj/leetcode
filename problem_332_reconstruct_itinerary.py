import collections
from typing import List


class Solution:
    def findItinerary01(self, tickets: List[List[str]]) -> List[str]:
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        route = []
        graph = collections.defaultdict(list)

        # create graph
        for a, b in sorted(tickets):
            graph[a].append(b)

        dfs("JFK")

        # reverse route
        return route[::-1]

    def findItinerary02(self, tickets: List[List[str]]) -> List[str]:
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        route = []
        graph = collections.defaultdict(list)
        # create graph with reversed order
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        dfs("JFK")

        # reverse route
        return route[::-1]

    def findItinerary03(self, tickets: List[List[str]]) -> List[str]:
        route, stack = [], ["JFK"]
        graph = collections.defaultdict(list)

        # create graph
        for a, b in sorted(tickets):
            graph[a].append(b)

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        # reverse route
        return route[::-1]


s = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(s.findItinerary01(tickets))
print(s.findItinerary02(tickets))
print(s.findItinerary03(tickets))
