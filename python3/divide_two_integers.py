"""
Space   : O(1)
Time    : O(log n)
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        is_neg = True if dividend < 0 else False
        is_neg ^= True if divisor < 0 else False

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans, count = 0, 1
        temp = divisor
        while (divisor << 1) <= dividend:
            divisor <<= 1
            count *= 2

        while dividend >= divisor and dividend > 0:
            dividend -= divisor
            ans += count
            while dividend < divisor:
                divisor >>= 1
                count >>= 1
            if divisor < temp:
                break

        if is_neg:
            return -1 * min(ans, (2 ** 31))

        return min(ans, (2**31) - 1)
