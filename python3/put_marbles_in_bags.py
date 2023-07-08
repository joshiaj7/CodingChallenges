from typing import List
from itertools import pairwise
from heapq import nlargest, nsmallest

class Solution:
    """
    Space   : O(n)
    Time    : O(n log k)
    """
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_sums = [a + b for a, b in pairwise(weights)]
        return sum(nlargest(k-1, pair_sums)) - sum(nsmallest(k-1, pair_sums))
    
    """
    Space   : O(n)
    Time    : O(n log n)
    """
    def putMarblesSort(self, weights: List[int], k: int) -> int:
        ans = 0
        n = len(weights)
        pair_weights = []
        for i in range(n-1):
            pair_weights.append(weights[i] + weights[i+1])
        pair_weights.sort()

        for i in range(k-1):
            ans += pair_weights[n-2-i] - pair_weights[i]

        return ans
