import math
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)

        for s,e in roads:
            graph[s].append(e)
            graph[e].append(s)

        def dfs(origin, prior):
            count = 1
            for dest in graph[origin]:
                if dest == prior:
                    continue
                count += dfs(dest, origin)

            if origin != 0:
                self.ans += math.ceil(count / seats)
            return count

        self.ans = 0
        dfs(0, -1)

        return self.ans
