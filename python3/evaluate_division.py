from collections import defaultdict, deque

"""
Space   : O(n**2)
Time    : O(n**2)

Method:
Graph - BFS
"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        ans = []

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1/val
        ans = []

        for a, b in queries:
            queue = deque()
            visited = set()
            curr = -1
            if a in graph:
                queue.append((a, 1))
                visited.add(a)
            while queue:
                i, value = queue.popleft()
                if i == b:
                    curr = value
                    break
                for j, valj in graph[i].items():
                    if j not in visited:
                        queue.append((j, value*valj))
                        visited.add(j)
            ans.append(curr)

        return ans
