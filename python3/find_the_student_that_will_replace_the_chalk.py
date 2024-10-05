from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sumC = sum(chalk)
        k = k % sumC

        for i, v in enumerate(chalk):
            if k < v:
                return i

            k -= v

        return -1
        