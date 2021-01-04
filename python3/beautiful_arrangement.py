"""
Permutation approach
Space   : O(n)
Time    : O(n!)
"""

class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        
        def dfs(i, cands):
            nonlocal ans
            if i <= 1:
                ans += 1
                return
            for j, x in enumerate(cands):
                if i % x == 0 or x % i == 0:
                    dfs(i-1, cands[:j] + cands[j+1:])
                    
        dfs(n, list(range(1, n+1)))
        return ans