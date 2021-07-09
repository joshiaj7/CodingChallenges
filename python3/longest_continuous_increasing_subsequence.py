# Space : O(1)
# Time  : O(n)

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s, ans = 0, 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                ans = max(ans, i-s+1)
            else:
                s = i

        return ans
