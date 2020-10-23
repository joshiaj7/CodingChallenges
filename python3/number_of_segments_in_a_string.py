"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        if s == '':
            return 0
        temp = s.split(' ')

        n = len(temp)
        ans = 0
        for i in range(n):
            if temp[i] != '':
                ans += 1

        return ans
