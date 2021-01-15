"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        longest = 0
        n = len(nums)
        k = sum(nums) - x
        d = {}
        d[0] = 0

        if k == 0:
            return len(nums)

        i, count = 0, 0
        while i < n:
            count += nums[i]
            d[count] = i+1

            if count - k in d:
                longest = max(longest, i - d[count-k]+1)

            i += 1

        if longest > 0:
            return n - longest

        return -1
