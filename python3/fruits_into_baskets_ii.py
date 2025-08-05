from typing import List

"""
Space   : O(1)
Time    : O(n ^ 2)
"""

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        n = len(baskets)

        for j in range(n):

            placed = False
            for i in range(n):
                if baskets[j] < fruits[i] or fruits[i] == -1:
                    continue
                else:
                    placed = True
                    fruits[i] = -1
                    break

            if not placed:
                ans += 1

        return ans

        