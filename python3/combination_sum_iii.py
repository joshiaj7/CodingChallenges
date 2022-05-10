from itertools import combinations

"""
Space   : O(n)
Time    : O(n!)
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        for item in combinations(range(1, 10), k):
            temp = list(item)
            if sum(temp) == n:
                ans.append(temp)

        return ans

    def combinationSum3NoCheat(self, k: int, n: int) -> List[List[int]]:
        def combine(start, end, path):
            if len(path) == k:
                if sum(path) == n:
                    ans.append(path)
                return
            for i in range(start, end):
                combine(i+1, end, path + [i])

        ans = []
        if sum(range(1, k+1)) > n or sum(range(10-k, 10)) < n:
            return []

        combine(1, 10, [])
        return ans
