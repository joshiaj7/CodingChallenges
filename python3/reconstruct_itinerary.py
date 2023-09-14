from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in sorted(tickets)[::-1]:
            graph[u].append(v)

        ans = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            ans.append(airport)
        
        dfs("JFK")
        return ans[::-1]
        