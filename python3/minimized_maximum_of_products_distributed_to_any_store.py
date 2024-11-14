from typing import List

"""
Space   : O(1)
Time    : O(m log n)
"""


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        ans = 0

        m = len(quantities)
        left = 1
        right = max(quantities)
        ans = right
        
        if m == n:
            return right

        while left <= right:
            mid = (left + right) // 2

            distributable = True
            count = 0
            for x in quantities:
                div = x // mid
                rem = x % mid

                count += div
                if rem > 0:
                    count += 1

                if count > n:
                    distributable = False
                    break

            if not distributable:
                left = mid + 1
            else:
                ans = min(ans, mid)
                right = mid - 1
                
        return ans
        