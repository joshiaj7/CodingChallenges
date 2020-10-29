"""
Space   : O(1)
Time    : O(log n)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        s, e = 0, x

        while True:
            mid = (s + e) // 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                if (mid+1)**2 > x:
                    return mid
                else:
                    s = mid
            else:
                e = mid
