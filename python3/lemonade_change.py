from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {
            5: 0,
            10: 0,
            20: 0,
        }

        for x in bills:
            if x == 5:
                cash[5] += 1
            elif x == 10:
                if cash[5] == 0:
                    return False
                cash[5] -= 1
                cash[10] += 1
            else:
                if cash[10] >= 1 and cash[5] >= 1:
                    cash[5] -= 1
                    cash[10] -= 1
                    cash[20] += 1
                elif cash[5] >= 3:
                    cash[5] -= 3
                    cash[20] += 1
                else:
                    return False

        return True
        