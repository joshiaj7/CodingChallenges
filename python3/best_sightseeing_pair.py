from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        n = len(values)

        ipair = []
        for i, v in enumerate(values): 
            ipair.append(i + v)

        for i in range(1, n):
            ipair[i] = max(ipair[i], ipair[i-1])

        for j in range(1, n):
            ans = max(ans, ipair[j-1] + values[j] - j)

        return ans
        