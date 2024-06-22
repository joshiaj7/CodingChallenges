from typing import List

"""
Space   : O(n)
Time    : O(n)
Sliding window
"""



class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        prefixes = [0] * (n + 1)
        prefixes[0] = 1

        for i in range(n):
            nums[i] %= 2

        s = 0
        for num in nums:
            s += num
            if s >= k:
                ans += prefixes[s - k]
            prefixes[s] += 1

        return ans
        