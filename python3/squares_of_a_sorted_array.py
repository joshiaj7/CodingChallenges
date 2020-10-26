"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []

        for i in A:
            ans.append(i**2)

        return sorted(ans)
