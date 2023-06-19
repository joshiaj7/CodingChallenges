"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        gain = [0] + gain
        n = len(gain)

        for i in range(1, n):
            gain[i] += gain[i-1]
            ans = max(ans, gain[i])

        return ans
