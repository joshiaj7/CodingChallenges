from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        dist_map = {}
        for start, end, dist in roads:
            graph[start].append(end)
            graph[end].append(start)
            dist_map[(start, end)] = dist
            dist_map[(end, start)] = dist

        visited = set()
        stack = [1]
        distances = []

        while stack:
            temp = []
            for start_node in stack:
                visited.add(start_node)
                for end_node in graph[start_node]:
                    if end_node in visited:
                        continue
                    temp.append(end_node)
                    distances.append(dist_map[(start_node, end_node)])

            stack = temp

        return min(distances)
