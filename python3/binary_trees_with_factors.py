"""
Space   : O(n)
Time    : O(n^2)
"""


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        arr.sort()

        for x in arr:
            dp[x] = 1

        for i, a in enumerate(arr):
            for b in arr[0:i]:
                if a % b == 0:
                    c = a // b
                    if c in dp:
                        dp[a] += dp[b] * dp[c]

        return sum(dp.values()) % 1000000007
