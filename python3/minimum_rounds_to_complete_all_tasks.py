"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        d = {}

        for t in tasks:
            if t in d:
                d[t] += 1
            else:
                d[t] = 1

        for v in d.values():
            if v == 1:
                return -1
            
            if v % 3 == 0:
                ans += v // 3
            else:
                ans += (v // 3) + 1

        return ans
