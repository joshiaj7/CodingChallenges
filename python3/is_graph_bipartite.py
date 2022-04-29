import collections

"""
Space : O(n)
Time  : O(n^2)

BFS approach
Method:
Graph coloring

alternatively you can use deque
for better pop time performance
"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n, colored = len(graph), {}
        for i in range(n):
            if i not in colored and graph[i]:
                colored[i] = 1
                q = collections.deque([i])
                while q:
                    cur = q.popleft()
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = -colored[cur]
                            q.append(nb)
                        elif colored[nb] == colored[cur]:
                            return False
        return True
