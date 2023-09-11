from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        hmap = defaultdict(list)

        for i, v in enumerate(groupSizes):
            hmap[v].append(i)

        for k, idx_list in hmap.items():
            group = []
            for i in idx_list:
                if len(group) > 0 and len(group) % k == 0:
                    ans.append(group)
                    group = []

                group.append(i)

            if len(group) > 0:
                ans.append(group)
                group = []


        return ans
