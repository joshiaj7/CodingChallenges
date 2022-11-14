from collections import defaultdict

"""
Space   : O(nm)
Time    : O(nm)
"""


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x, y):
            nonlocal visited
            if (x, y) not in visited:
                visited.add((x, y))
                for dy in graphX[x]:
                    dfs(x, dy)
                for dx in graphY[y]:
                    dfs(dx, y)

        graphX = defaultdict(list)
        graphY = defaultdict(list)
        for x, y in stones:
            graphX[x].append(y)
            graphY[y].append(x)
        
        visited = set()
        connected = 0
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                connected += 1

        return len(stones) - connected
