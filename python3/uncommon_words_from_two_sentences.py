from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        h1 = {}
        h2 = {}

        for x in s1.split(" "):
            if x in h1:
                h1[x] += 1
            else:
                h1[x] = 1

        for x in s2.split(" "):
            if x in h2:
                h2[x] += 1
            else:
                h2[x] = 1

        for k, v in h1.items():
            if v > 1 or k in h2:
                continue
            else:
                ans.append(k)

        for k, v in h2.items():
            if v > 1 or k in h1:
                continue
            else:
                ans.append(k)

        return ans
