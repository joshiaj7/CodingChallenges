from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = sorted(zip(names, heights), key=lambda x: -x[1])
        ans = []

        for name, _ in pair:
            ans.append(name)

        return ans
