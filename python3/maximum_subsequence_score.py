from typing import List
from heapq import heappop, heappush

"""
Space   : O(n + k)
Time    : O(n log n + n * (2 log k))
"""

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        n = len(nums1)

        nums = [(nums1[i], nums2[i]) for i in range(n)]
        nums.sort(key=lambda x: -x[1] )

        heap = []
        total = 0
        for val, mul in nums:
            heappush(heap, val)
            total += val
            
            if len(heap) > k:
                total -= heappop(heap)

            if len(heap) == k:
                ans = max(ans, total * mul)

        return ans
