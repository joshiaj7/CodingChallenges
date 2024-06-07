from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0

        freqMap = {}
        for x in nums:
            if x in freqMap:
                freqMap[x] += 1
            else:
                freqMap[x] = 1

        maxFreq = max(freqMap.values())
        for v in freqMap.values():
            if v == maxFreq:
                ans += v

        return ans
        
        