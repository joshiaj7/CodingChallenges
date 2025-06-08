from typing import List

"""
Space   : O(n)
Time    : O(n^3)
"""

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        n = len(digits)

        num = 0
        for i in range(n):
            num = 0
            if digits[i] % 2 == 1:
                continue
            num += digits[i]

            for j in range(n):
                if i == j:
                    continue

                num += digits[j] * 10
                for k in range(n):
                    if k == i or k == j or digits[k] == 0:
                        continue
                    
                    num += digits[k] * 100
                    ans.add(num)
                    num -= digits[k] * 100

                num -= digits[j] * 10
            num -= digits[i]
            
        return sorted(list(ans))
