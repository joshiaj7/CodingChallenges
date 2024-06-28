from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        graph = [0 for _ in range(n)]

        for u, v in roads:
            graph[u] += 1
            graph[v] += 1

        graph.sort()
        for i, v in enumerate(graph):
            ans += v * (i+1)

        return ans
