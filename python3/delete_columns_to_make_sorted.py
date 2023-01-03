"""
Space   : O(1)
Time    : O(mn)
"""

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        m, n = len(strs), len(strs[0])

        for i in range(n):
            is_sorted = True
            for j in range(1, m):
                if strs[j-1][i] > strs[j][i]:
                    is_sorted = False
                    break

            if not is_sorted:
                ans += 1

        return ans
