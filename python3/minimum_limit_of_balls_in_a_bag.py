from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            ops = 0
            mid = (left + right) // 2

            for x in nums:
                div = (x - 1) // mid
                ops += div

            if ops > maxOperations:
                left = mid + 1
            else:
                right = mid

        return right
        