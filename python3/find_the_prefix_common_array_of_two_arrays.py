from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n^2)
"""


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        da = defaultdict(bool)
        db = defaultdict(bool)
        n = len(A)

        for i in range(n):
            da[A[i]] = True
            db[B[i]] = True

            count = 0
            for k in da.keys():
                if k in db:
                    count += 1

            ans.append(count)

        return ans
