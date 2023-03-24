from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0

        original_path = set()
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            original_path.add((u, v))

        stack = [0]
        visited = set()
        while stack:
            temp = []
            for node in stack:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue

                    if (node, neighbor) in original_path:
                        ans += 1

                    temp.append(neighbor)
                
            stack = temp

        return ans
