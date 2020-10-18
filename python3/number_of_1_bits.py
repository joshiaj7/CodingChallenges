"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        binary = bin(n)[2:]
        n = len(binary)

        for i in binary:
            if i == '1':
                ans += 1

        return ans
