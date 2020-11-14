"""
Space   : O(n)
Time    : O(n)
Hackerrank competition
"""


def getMinimumUniqueSum(arr):
    ans = 0
    dp = [0] * 7000
    for i in arr:
        dp[i] += 1

    n = len(dp)
    for i in range(n-1):
        if dp[i] > 1:
            dp[i+1] += dp[i] - 1
            dp[i] = 1

    for j in range(n):
        if dp[j] > 0:
            ans += j

    return ans
