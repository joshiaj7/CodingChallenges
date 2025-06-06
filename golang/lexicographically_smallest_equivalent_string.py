from collections import defaultdict

"""
Space   : O(26 + n)
Time    : O(n + m * 26)
n = len(s1)
m = len(baseStr)
"""

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ans = []
        n = len(s1)
        d = defaultdict(list)

        for i in range(n):
            d[s1[i]].append(s2[i])
            d[s2[i]].append(s1[i])

        
        def dfs(c, visited):
            visited.add(c)
            min_c = c
            for item in d[c]:
                if item not in visited:
                    candidate = dfs(item, visited)
                    min_c = min(min_c, candidate)
            return min_c

        for c in baseStr:
            visited = set()
            ans.append(dfs(c, visited))

        return "".join(ans)

class Solution:
    def smallestEquivalentStringUF(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}
        n = len(s1)

        def find(x):
            if x not in UF:
                UF[x] = x

            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX > rootY:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX

        for i in range(n):
            union(s1[i], s2[i])

        ans = []
        for c in baseStr:
            ans.append(find(c))

        return "".join(ans)
