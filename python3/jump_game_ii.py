# Space : O(n)
# Time  : O(n**2)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10**5] * n
        dp[0] = 0
        
        if n == 1:
            return 0
        
        for i in range(n):
            for j in range(nums[i]):
                dp[j+i+1] = min(dp[j+i+1], dp[i] + 1)
                if j+i+1 == n-1:
                    return dp[-1]

        return dp[-1]