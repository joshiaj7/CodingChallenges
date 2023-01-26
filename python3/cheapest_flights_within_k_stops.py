from collections import defaultdict
from heapq import heappop, heappush

"""
Space   : O(2^n)
Time    : O(2^n)
"""

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        visited = {}
        graph = defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        heap = [(0, 0, src)]
        while heap:
            dist, moves, node = heappop(heap)
            if node == dst and K >= moves - 1:
                return dist
            if node not in visited or visited[node] > moves:
                visited[node] = moves
                for nei, weight in graph[node]:
                    heappush(heap, (dist + weight, moves + 1, nei))
        return -1
