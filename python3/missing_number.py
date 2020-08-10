# leetcode

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        search = 0
        
        while True:
            if search not in nums:
                return search
            else:
                search += 1