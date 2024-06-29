from typing import List
from collections import defaultdict

"""
Space   : O(n + m)
Time    : O(n * k log k)
"""


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)

        for i in range(n):
            self.dfs(graph, i, i, ans, [False]*n)

        for i in range(n):
            ans[i].sort()

        return ans

    def dfs(self, graph, parent, curr, ans, visit):
        visit[curr] = True
        for dest in graph[curr]:
            if not visit[dest]:
                ans[dest].append(parent)
                self.dfs(graph, parent, dest, ans, visit)
