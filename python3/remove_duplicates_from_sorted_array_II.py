# Space   : O(1)
# Time    : O(n)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return n
        
        i = 0
        while i < len(nums) - 2:
            while nums[i] == nums[i+2]:
                nums.pop(i)
                if i >= len(nums)-2:
                    break
                      
            i += 1
        
        return len(nums)
        