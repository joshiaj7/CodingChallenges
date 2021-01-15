"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0] * max(n+1, 2)
        arr[0] = 0
        arr[1] = 1

        if n <= 1:
            return arr[n]

        ans = 0

        for i in range(2, n+1):
            if i % 2 == 0:
                arr[i] = arr[i//2]
            else:
                arr[i] = arr[i//2] + arr[i//2 + 1]
            ans = max(ans, arr[i])

        return ans
