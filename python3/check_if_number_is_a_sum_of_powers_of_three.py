"""
Space   : O(1)
Time    : O(log3n)
"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        num = n
        res = ""
        while num > 0:
            x = num % 3
            num //= 3
            res += str(x)

        for c in res:
            if c == '2':
                return False

        return True
