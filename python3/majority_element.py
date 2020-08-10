# leetcode

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        leng = len(nums)
        if leng % 2 == 1:
            mid = (leng // 2) + 1
        else:
            mid = leng // 2
            
        mem = {}
        
        for i in nums:
            if i in mem:
                mem[i] += 1
            else:
                mem[i] = 1
        
        ans = 0
        for key, val in mem.items():
            if val >= mid:
                ans = key

        return ans