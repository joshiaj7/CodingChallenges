from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return informTime[0]
        
        ans = []
        graph = defaultdict(list)

        for i, val in enumerate(manager):
            if val == -1:
                continue
            graph[val].append(i)

        stack = [(headID, 0)]
        while stack:
            temp = []
            for person, time in stack:
                if person in graph:
                    for subordinate in graph[person]:
                        temp.append((subordinate, time + informTime[person]))
                else:
                    ans.append(time)
            
            stack = temp

        return max(ans)
