"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
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
