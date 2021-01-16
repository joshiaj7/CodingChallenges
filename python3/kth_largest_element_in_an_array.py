"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
