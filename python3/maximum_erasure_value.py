"""
Space   : O(n)
Time    : O(n)

Method:
two pointers with dp
"""


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = start = count = 0
        n = len(nums)
        dp = [0]
        mem = {}

        for i, val in enumerate(nums):
            count += val
            dp.append(count)
            if val in mem and start <= mem[val]:
                start = mem[val] + 1
            else:
                ans = max(ans, count - dp[start])
            mem[val] = i

        return ans
