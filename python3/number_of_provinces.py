from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n^2 + n)
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        memo = [-1 for _ in range(n)]
        graph = defaultdict(set)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    graph[i].add(j)

        def bfs(i):
            stack = [i]
            while stack:
                temp = []
                for node in stack:
                    memo[node] = i
                    for neighbor in graph[node]:
                        if memo[neighbor] == -1:
                            temp.append(neighbor)
                stack = temp

        for i in range(n):
            if memo[i] == -1:
                bfs(i)

        return len(set(memo))
