from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = []
        rankMap = {}

        temp = arr[::]
        temp.sort()

        rank = 1
        for x in temp:
            if x not in rankMap:
                rankMap[x] = rank
                rank += 1

        for x in arr:
            ans.append(rankMap[x])

        return ans
        