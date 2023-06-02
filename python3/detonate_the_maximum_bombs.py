from typing import List
from collections import defaultdict

"""
Space   : O(n^2)
Time    : O(n^3)
"""

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        ans = 0
        memo = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2]**2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    memo[i].append(j)


        def dfs(i, visited):
            for neighbor in memo[i]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))

        return ans
