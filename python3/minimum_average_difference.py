"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        min_avg = float('inf')
        ans = 0

        left, right = 0, s
        cl, cr = 0, n
        for i in range(n):
            left += nums[i]
            right -= nums[i]
            cl += 1
            cr -= 1

            if i == n-1:
                a = (left // cl) - (right)
            else:
                a = (left // cl) - (right // cr)

            if abs(a) < min_avg:
                min_avg = abs(a)
                ans = i

        return ans
