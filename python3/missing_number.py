# Space : O(1)
# Time  : O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_nums, total_idx = 0, 0

        for i in range(len(nums)):
            total_nums += nums[i]
            total_idx += i + 1

        return total_idx - total_nums
