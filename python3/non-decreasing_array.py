# Space   : O(1)
# Time    : O(n)


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        forward, backward = 0, 0
        fmax, bmin = nums[0], nums[-1]
    
        # forward
        for i in range(1, n):
            if fmax > nums[i]:
                forward += 1
            fmax = max(fmax, nums[i])
        
        # backward
        for i in range(n-2, -1, -1):
            if bmin < nums[i]:
                backward+=1 
            bmin = min(bmin, nums[i])
            
        return min(forward, backward) <= 1