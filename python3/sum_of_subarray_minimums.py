"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        n = len(arr)
        dp = [0] * n
        stack = [0]

        for i in range(n):
            while arr[stack[-1]] > arr[i]:
                stack.pop()

            j = stack[-1]
            dp[i] = dp[j] + (i - j) * arr[i]
            stack.append(i)

        return sum(dp) % (10**9 + 7)
