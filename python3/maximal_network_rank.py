from typing import List
from collections import defaultdict

"""
Space   : O(n^2)
Time    : O(n^2)
"""

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        graph = defaultdict(set)

        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)

        for u in range(n):
            for v in range(u+1, n):
                if v in graph[u]:
                    ans = max(ans, len(graph[u]) + len(graph[v]) - 1)
                else:
                    ans = max(ans, len(graph[u]) + len(graph[v]))

        return ans


# codility SN

def solution(A, B, N):
    ans = 0
    graph = defaultdict(set)

    for u, v in zip(A, B):
        graph[u].add(v)
        graph[v].add(u)

    visited = set()
    for u in range(1, N):
        for v in graph[u]:
            if (u, v) in visited or (v, u) in visited:
                continue
                
            visited.add((u, v))
            ans = max(ans, len(graph[u]) + len(graph[v]) - 1)

    return ans
