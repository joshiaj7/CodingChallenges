# leetcode

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, dp = 0, 0
        
        for i in nums:
            if i == 1:
                ans += 1
                dp = max(dp, ans)
            else:
                ans = 0
            
        return dp