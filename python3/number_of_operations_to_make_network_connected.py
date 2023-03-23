from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        graph = defaultdict(list)
        for start, end in connections:
            graph[start].append(end)
            graph[end].append(start)

        visited = [0] * n

        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = 1
            for neighbor in graph[node]:
                dfs(neighbor)
            return 1

        result = 0
        for i in range(n):
            result += dfs(i)
        
        return result - 1
