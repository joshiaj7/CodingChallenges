# leetcode

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        leng = len(nums)
        
        for idx in range(leng):
            if nums[idx] == target:
                break
            elif nums[idx] > target:
                break
            ans += 1
                
        return ans