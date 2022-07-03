"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        disc = []
        for i in range(1, n):
            disc.append(nums[i] - nums[i-1])

        ans = last = 0
        for i, v in enumerate(disc):
            if (last > 0 and v > 0) or (last < 0 and v < 0) or (v == 0):
                continue

            ans += 1
            last = v

        return ans + 1
