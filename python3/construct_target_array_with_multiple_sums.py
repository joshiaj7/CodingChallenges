from heapq import heappush, heappop, heapify

"""
Space   : O(n)
Time    : O(n log n)

Method:
heap (using %)
"""


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-x for x in target]
        heapify(heap)

        while True:
            num = -heappop(heap)
            total -= num
            if num == 1 or total == 1:
                return True
            if num < total or total == 0 or num % total == 0:
                return False
            num %= total
            total += num
            heappush(heap, -num)
