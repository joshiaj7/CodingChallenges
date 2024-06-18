from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0
        p = sorted(zip(difficulty, profit), key=lambda x: -x[1])
        w = sorted(worker, key=lambda x: -x)

        np = len(p)

        pairp = 0

        for v in w:
            while pairp < np and p[pairp][0] > v:
                pairp += 1

            if pairp == np:
                ans += 0
            else:
                ans += p[pairp][1]

        return ans
