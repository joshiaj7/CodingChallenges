from collections import defaultdict
from typing import List

"""
Space   : O(2^n)
Time    : O(2^n)
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        d = defaultdict(list)

        for i, v in enumerate(graph):
            d[i] = (v)

        def dfs(path):
            k = path[-1]
            if k == n-1:
                ans.append(path)
            else:
                for node in d[k]:
                    if node not in path:
                        dfs(path + [node])

        dfs([0])
        return ans
