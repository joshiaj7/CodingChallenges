from heapq import heappush, heappop

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        heap = []

        for p in piles:
            heappush(heap, -p)

        while k > 0:
            stones = -heappop(heap)
            disc = stones // 2
            heappush(heap, -stones + disc)
            k -= 1

        return -sum(heap)
