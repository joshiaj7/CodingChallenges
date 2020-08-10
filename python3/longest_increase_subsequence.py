# leetcode

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        leng = len(nums)
        lis = [1] * leng
        
        for i in range(1, leng):
            # print(lis)
            for j in range(0, i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j]+1)
        
        print(lis)
        return max(lis)
        
        
        