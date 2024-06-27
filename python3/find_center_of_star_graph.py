from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = defaultdict(list)
        n = len(edges)

        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        for k, v in nodes.items():
            if len(v) == n:
                return k 

        return -1
        