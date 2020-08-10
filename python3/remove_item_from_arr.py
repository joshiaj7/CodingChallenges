class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leng = len(nums)
        unique = 0
        memo = []
        
        for idx in range(leng):
            if nums[idx] != val:
                unique += 1
                memo.append(nums[idx])
                
        print(memo)
        print(unique)
        
        for i in range(len(memo)):
            nums[i] = memo[i] 
                
        
        return unique
        