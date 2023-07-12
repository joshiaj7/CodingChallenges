from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        ans = []

        indegrees = defaultdict(list)
        outdegree = defaultdict(int)
        queue = []

        for u in range(n):
            outdegree[u] = len(graph[u])
            if len(graph[u]) == 0:
                queue.append(u)

            for v in graph[u]:
                indegrees[v].append(u)

        while queue:
            node = queue.pop(0)
            ans.append(node)

            for indeg in indegrees[node]:
                outdegree[indeg] -= 1
                if outdegree[indeg] == 0:
                    queue.append(indeg)

        return sorted(ans)
