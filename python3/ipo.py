from heapq import heappush, heappop

"""
Space   : O(n)
Time    : O(k * len(n))
"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = sorted(zip(profits, capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:
                heappush(heap, -projects[i][0])
                i += 1
            if heap: 
                w -= heappop(heap)
        return w
