# Space : O(1)
# Time  : O(n)

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        ans = 0

        for x in nums:
            ans += x - min_num

        return ans
