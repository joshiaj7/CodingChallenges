class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        latest = -100000000000000000000000000
        idx = 0
        while idx < len(nums):
            if latest != nums[idx]:
                latest = nums[idx]
                idx += 1
            elif nums[idx] == latest:
                del nums[idx]
            else:
                idx += 1
            
        return len(nums)