from typing import List
from heapq import heapify, heappush, heappop

"""
Space   : O(candidates * 2)
Time    : O(k * log n)
"""


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        n = len(costs)
        first_batch = costs[:candidates]
        second_batch = costs[max(candidates, n-candidates):]

        heapify(first_batch)
        heapify(second_batch)

        first, second = candidates, n-candidates-1
        for _ in range(k):
            if not second_batch or (first_batch and first_batch[0] <= second_batch[0]):
                ans += heappop(first_batch)
                if first <= second:
                    heappush(first_batch, costs[first])
                    first += 1
            else:
                ans += heappop(second_batch)
                if first <= second:
                    heappush(second_batch, costs[second])
                    second -= 1


        return ans
