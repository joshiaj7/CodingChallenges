"""
Space   : O(n)
Time    : O(n^2)
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        arr = list(str(num))
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                arr[i], arr[j] = arr[j], arr[i]
                newNum = int("".join(arr))
                ans = max(ans, newNum)
                arr[i], arr[j] = arr[j], arr[i]

        return ans
