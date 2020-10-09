"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ''
        multi = 1

        isNeg = num < 0
        num = abs(num)

        while multi * 7 <= num:
            multi *= 7

        while multi >= 1:
            ans += str(num // multi)
            if num >= 0:
                num = int(num % multi)
            else:
                ans += str(num)
            multi //= 7

        if isNeg:
            ans = '-' + ans

        return ans
