from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}

        for x in arr:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        dis = []
        for x in arr:
            if d[x] == 1:
                dis.append(x)

        if len(dis) < k:
            return ""

        return dis[k-1]
        