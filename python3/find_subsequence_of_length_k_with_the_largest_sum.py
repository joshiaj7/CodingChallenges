from collections import List

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        
        numsWithIdx = []
        for i in range(n):
            numsWithIdx.append((nums[i], i))

        numsWithIdx.sort(key=lambda x: -x[0])

        subArr = numsWithIdx[:k]
        subArr.sort(key=lambda x: x[1])
        
        for v, _ in subArr:
            ans.append(v)

        return ans
