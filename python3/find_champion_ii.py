from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champs = []
        g = defaultdict(list)

        for u, v in edges:
            g[v].append(u)

        for i in range(n):
            if i not in g:
                champs.append(i)

        if len(champs) > 1:
            return -1

        return champs[0]
