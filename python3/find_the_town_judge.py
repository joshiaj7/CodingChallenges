from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        g1, g2 = defaultdict(list), defaultdict(list)

        for a, b in trust:
            g1[a].append(b)
            g2[b].append(a)

        for i in range(1, n+1):
            if i not in g1 and len(g2[i]) == n - 1:
                return i

        return -1
