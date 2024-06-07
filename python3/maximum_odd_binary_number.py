"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        n = len(s)

        for l in s:
            if l == "1":
                ones += 1

        return "1" * (ones-1) + "0" * (n-ones) + "1"
