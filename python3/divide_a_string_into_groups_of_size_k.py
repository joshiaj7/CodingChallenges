from collections import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []

        temp = ""
        for l in s:
            temp += l

            if len(temp) == k:
                ans.append(temp)
                temp = ""

        if len(temp) > 0:
            temp += fill * (k - len(temp))
            ans.append(temp)

        return ans
        