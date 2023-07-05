from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        count = 0
        group = []
        for x in nums:
            if x == 1:
                count += 1
            else:
                if count > 0:
                    group.append(count)
                group.append(0)
                count = 0

        if count > 0:
            group.append(count)

        if len(group) == 1:
            return group[0] - 1

        g = len(group)
        for i in range(g):
            if i == 0:
                ans = max(ans, group[i+1])
            elif i == g-1:
                ans = max(ans, group[i-1])
            else:
                ans = max(ans, group[i-1] + group[i+1])

        return ans
