# Space : O(1)
# Time  : O(n log n)

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        if n <= 1:
            return 0

        nums.sort()

        for i in range(1, n):
            ans = max(ans, nums[i] - nums[i-1])

        return ans
