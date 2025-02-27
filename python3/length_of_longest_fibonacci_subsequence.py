
from typing import List

"""
Space   : O(n)
Time    : O(n^2)
"""

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)

        h = set(arr)
        for i in range(n):
            for j in range(i+1, n):
                a = arr[i]
                b = arr[j]
                longest = 2

                while a + b in h:
                    longest += 1
                    if longest % 2 == 1:
                        a += b
                    else:
                        b += a

                if longest > 2:
                    ans = max(ans, longest)

        return ans
        