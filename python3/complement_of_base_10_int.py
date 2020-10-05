"""
Space   : O(n)
Time    : O(1)
"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n = len(bin(N)[2:])
        return (int('1'*n, 2) ^ N)
