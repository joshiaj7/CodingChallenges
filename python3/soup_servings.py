import math

"""
Space   : O(200 ^ 2)
Time    : O(200 ^ 2)
"""

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1

        memo = {}
        def calculate(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            if a <= 0 and b <= 0:
                return 0.5

            if a <= 0:
                return 1

            if b <= 0:
                return 0

            memo[(a, b)] = 0.25 * (calculate(a - 4, b) + calculate(a - 3, b - 1) + calculate(a - 2, b - 2) + calculate(a - 1, b - 3))
            return memo[(a, b)]
        

        n = math.ceil(n / 25.0)
        return calculate(n, n)
