from typing import List

"""
Space   : O(k)
Time    : O(n)
Sliding window
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        d = {}
        cumsum = 0

        # window
        for i, x in enumerate(nums):
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
            cumsum += x

            # remove excess window
            if i >= k:
                y = nums[i-k]
                if d[y] > 1:
                    d[y] -= 1
                else:
                    del d[y]
                cumsum -= y

            # window fulfilled
            if i >= k-1:
                if len(d) == k:
                    ans = max(ans, cumsum)

        return ans
        