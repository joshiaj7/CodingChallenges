"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # tortoise and hare algorithm
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow