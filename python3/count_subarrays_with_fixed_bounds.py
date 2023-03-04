"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        jmin = jmax = jbad = -1
        for i, x in enumerate(nums):
            if not minK <= x <= maxK: 
                jbad = i
            if x == minK: 
                jmin = i
            if x == maxK: 
                jmax = i
            ans += max(0, min(jmin, jmax) - jbad)
        return ans
