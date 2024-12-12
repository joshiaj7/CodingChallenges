from typing import List
from heapq import heappush, heappop
import math

"""
Space   : O(n)
Time    : O(k log n)
"""

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for g in gifts:
            heappush(heap, -g)

        for _ in range(k):
            g = -heappop(heap)
            sqrted = math.floor(math.sqrt(g))
            heappush(heap, -sqrted)

        return -sum(heap)
        