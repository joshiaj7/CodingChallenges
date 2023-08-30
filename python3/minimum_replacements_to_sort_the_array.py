"""
Space   : O(1)
Time    : O(n)

Google interview question
"""

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        x = nums[-1]
        n = len(nums)
        ans = 0

        for i in range(n -1, -1, -1):
            k = (nums[i] + x - 1) // x
            x = nums[i] // k
            ans += k - 1
            
        return ans
