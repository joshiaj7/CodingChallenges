from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        avail = set()

        allUnique = True
        for i in range(n-1, -1, -1):
            if nums[i] in avail:
                allUnique = False
                break
            avail.add(nums[i])

        if allUnique:
            return 0

        ans = (i+1) // 3
        if (i+1) % 3 > 0:
            ans += 1

        return ans
        