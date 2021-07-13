# Space : O(1)
# Time  : O(26 log n)

class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""

        while n > 0:
            n -= 1
            ans = chr(65+(n % 26)) + ans
            n //= 26

        return ans
