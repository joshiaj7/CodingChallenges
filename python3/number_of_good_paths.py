from collections import Counter

"""
Space   : O(union-find(n))
Time    : O(union-find(n))
"""

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ans = n = len(vals)
        UF = list(range(n))
        count = [Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([max(vals[i], vals[j]), i, j] for i, j in edges)

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]


        for m, i, j in edges:
            fi, fj = find(i), find(j)
            cj, ci = count[fi][m], count[fj][m]
            ans += ci * cj
            UF[fj] = fi
            count[fi] = Counter({m: ci + cj})

        return ans
