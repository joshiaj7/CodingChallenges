"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        slow, fast = 1, 1
        k = 1

        while slow < n and fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
                k += 1
            fast += 1

        return k
