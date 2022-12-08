import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        while len(graph) > 2:
            leaf = []
            for i in graph:
                if len(graph[i]) == 1:
                    leaf.append(i)
            for target in leaf:
                rem = graph[target].pop()
                graph[rem].remove(target)
                graph.pop(target)
        return list(graph.keys())


n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
edges1 = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
s = Solution()
print(s.findMinHeightTrees(n, edges))
print(s.findMinHeightTrees(n, edges1))
