# leetcode

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(nums) == len(set(nums)):
            return False

        for i, cur_val in enumerate(nums):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(cur_val - nums[j]) <= t:
                    return True

        return False
