"""
Space : O(n)
Time  : O(n)
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        d = {0: -1}
        count = 0
        
        for i in range(n):
            count = (count + nums[i]) % k
            
            if count not in d:
                d[count] = i
            elif i - d[count] >= 2:
                return True
            
        return False
