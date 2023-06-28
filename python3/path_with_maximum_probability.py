from typing import List
from collections import defaultdict
from heapq import heappop, heappush

"""
Space   : O(e)
Time    : O(e * log n)

where e = len(edges)
Shortest path djikstra
"""

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        prob = [0.0] * n

        for index, (a, b) in enumerate(edges):
            graph[a].append((b, index))
            graph[b].append((a, index))

        prob[start] = 1.0
        heap = [(-prob[start], start)]

        while heap:
            p, curr = heappop(heap)
            if curr == end:
                return -p

            for neighbor, index in graph.get(curr, []):
                if -p * succProb[index] > prob[neighbor]:
                    prob[neighbor] = -p * succProb[index]
                    heappush(heap, (-prob[neighbor], neighbor))

        return 0.0
