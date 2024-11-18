from typing import List

"""
Space   : O(n)
Time    : O(nk)
"""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0 for _ in range(n)]

        ans = []
        circular = code * 3
        for i in range(n, 2 * n):
            num = 0
            if k > 0:
                for j in range(1, k+1):
                    num += circular[i+j]
            else:
                for j in range(1, -k+1):
                    num += circular[i-j]
            ans.append(num)

        return ans
