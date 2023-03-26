from collections import defaultdict

"""
Space : O(n)
Time  : O(n)
"""

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ans = 0

        mem = [-1] * n
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, color):
            if mem[node] != -1:
                return 
            mem[node] = color
            for neighbor in graph[node]:
                dfs(neighbor, color)

        for i in range(n):
            dfs(i, i)

        node_colors = defaultdict(list)
        for i, c in enumerate(mem):
            node_colors[c].append(i)

        for v in node_colors.values():
            leng = len(v)
            ans += leng * (n - leng)
            n -= leng 

        return ans
