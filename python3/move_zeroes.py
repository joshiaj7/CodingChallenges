# leetcode

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero = 0
        idx = 0
        done = False
        
        while not done:
            if nums[idx] == 0:
                del nums[idx]
                nums.append(0)
                zero += 1
            else:
                idx += 1
            
            if idx == len(nums)-1 or idx == len(nums)-zero:
                done = True
