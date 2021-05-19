# Space : O(1)
# Time  : O(n log n)

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        nums.sort()
        median = ((nums[n//2] + nums[(n//2)-1]) // 2) if (n % 2 == 0) else nums[n//2]

        for x in nums:
            ans += abs(x - median)
        
        return ans