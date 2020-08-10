# leetcode

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        leng = len(nums)
        
        for i in nums:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            elif i == 2:
                two += 1
                  
        print(zero, one, two)
        
        idx = 0
        while idx < leng:
            if zero > 0:
                nums[idx] = 0
                zero -= 1
            elif one > 0:
                nums[idx] = 1
                one -= 1
            elif two > 0:
                nums[idx] = 2
                two -= 1
            idx += 1
            