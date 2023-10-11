from typing import List
from bisect import bisect_left, bisect_right

"""
Space   : O(n)
Time    : (n log n + m log n)
"""

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted(a for a, _ in flowers)
        end = sorted(b for _, b in flowers)

        return [bisect_right(start, t) - bisect_left(end, t) for t in people]
        