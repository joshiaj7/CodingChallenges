from typing import List

"""
Space   : O(k)
Time    : O(n * k)
"""


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        dist = [0] * k

        if len(cookies) == k:
            return max(cookies)

        def backtrack(i):
            nonlocal ans
            if i == len(cookies):
                ans = min(ans, max(dist))
                return
            
            for j in range(k):
                dist[j] += cookies[i]
                backtrack(i+1)
                dist[j] -= cookies[i]

        backtrack(0)
        return ans
