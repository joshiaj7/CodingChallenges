# Optimized dp-queue approach
# Space : O(n)
# Time  : O(n)

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        q = [0]

        for i in range(1, n):
            if q[0] < i-k:
                q = q[1:]
            dp[i] = nums[i] + dp[q[0]]
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)

        return dp[-1]
