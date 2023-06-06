from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr = sorted(arr)

        dif = 0
        for i in range(1, n):
            if i == 1:
                dif = arr[i] - arr[i-1]
                continue

            if arr[i] - arr[i-1] != dif:
                return False

        return True
