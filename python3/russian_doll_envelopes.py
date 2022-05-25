from bisect import bisect_left

"""
Space : O(n)
Time  : O(n log n)

Method:
DP with bisect
"""


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for _, h in envelopes:
            i = bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)
