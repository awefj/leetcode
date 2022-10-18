import collections
from typing import List


class Solution:
    def canFinish01(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            # circuit confirmed
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            return True

        graph = collections.defaultdict(list)
        traced = set()

        # create graph
        for x, y in prerequisites:
            graph[x].append(y)

        # check circuit
        for x in list(graph):
            if not dfs(x):
                return False
        return True

    def canFinish02(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            # circuit confirmed
            if i in traced:
                return False
            # already checked
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True

        graph = collections.defaultdict(list)
        traced, visited = set(), set()

        # create graph
        for x, y in prerequisites:
            graph[x].append(y)

        # check circuit
        for x in list(graph):
            if not dfs(x):
                return False
        return True


s = Solution()
prerequisites = [[1, 0], [0, 1]]
print(s.canFinish01(2, prerequisites))
print(s.canFinish02(2, prerequisites))
