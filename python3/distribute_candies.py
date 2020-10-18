from collections import Counter

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        n = len(candies)

        if n == 0:
            return 0

        c = Counter(candies)
        num = n // 2

        if len(c) >= num:
            return num

        return len(c)
