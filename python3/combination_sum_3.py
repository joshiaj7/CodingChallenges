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
