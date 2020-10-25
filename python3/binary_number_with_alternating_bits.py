"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n <= 1:
            return True

        bit = bin(n)[2:]

        truth = bit[0]

        for i in range(1, len(bit)):
            if bit[i] != truth:
                truth = bit[i]
            else:
                return False

        return True
