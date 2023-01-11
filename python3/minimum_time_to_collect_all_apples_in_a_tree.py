from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        def dfs(node, prev):
            for neighbor in graph[node]:
                if neighbor != prev and dfs(neighbor, node):
                    hasApple[node] = True
            return hasApple[node]

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        dfs(0, -1)
        return (sum(hasApple ) - hasApple[0]) * 2
