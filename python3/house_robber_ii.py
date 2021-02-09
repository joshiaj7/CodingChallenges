"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        
        ans = 0
        leng = len(nums)-1
        one, two = [0] * leng, [0] * leng
        
        # 1st iteration
        for idx in range(leng):
            if idx < 2:
                one[idx] = nums[idx]
            else:
                one[idx] = nums[idx] + max(one[idx-2], one[idx-3])
            ans = max(ans, one[idx])
        
        # 2nd iteration
        for idx in range(leng):
            if idx < 2:
                two[idx] = nums[idx+1]
            else:
                two[idx] = nums[idx+1] + max(two[idx-2], two[idx-3])
            ans = max(ans, two[idx])
        
        return ans
        