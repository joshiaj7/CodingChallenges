from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = [0, 0]

        for i in range(1, n+1):
            a = i
            b = n - a

            containsZero = False
            for d in str(a):
                if d == "0":
                    containsZero = True
                    break

            if containsZero:
                continue

            for d in str(b):
                if d == "0":
                    containsZero = True
                    break

            if containsZero:
                continue

            return [a, b]

        return ans
        