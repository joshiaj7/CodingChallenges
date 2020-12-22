"""
Best Solution
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        ans = A[-1] - A[0]
        for x, y in zip(A, A[1:]):
            ans = min(ans, max(A[-1]-K, x+K) - min(A[0]+K, y-K))
        return ans
