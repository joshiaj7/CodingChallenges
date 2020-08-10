# leetcode

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # tortoise and hare algorithm
        slow = nums[0]
        fast = nums[nums[0]]
        
        
        while slow != fast:
            print("slow: {}, fast: {}".format(slow, fast))
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        print("slow: {}, fast: {}".format(slow, fast))
        print("second loop")
        fast = 0
        while fast != slow:
            print("slow: {}, fast: {}".format(slow, fast))
            slow = nums[slow]
            fast = nums[fast]
        
        print("slow: {}, fast: {}".format(slow, fast))
        return slow