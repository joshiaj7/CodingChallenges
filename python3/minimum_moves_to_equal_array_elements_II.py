# Space : O(1)
# Time  : O(n log n)

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        nums.sort()

        if n % 2 == 0:
            median = (nums[n//2] + nums[(n//2) - 1]) // 2
        else:
            median = nums[n//2]

        for i in nums:
            ans += abs(i - median)

        return ans
