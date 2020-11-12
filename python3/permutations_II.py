"""
Space   : O(n)
Time    : O(n!)
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def getPermutation(nums, path):
            if not nums:
                result.append(path)
            for i, v in enumerate(nums):
                if i > 0 and v == nums[i-1]:
                    continue
                getPermutation(nums[:i] + nums[i+1:], path + [nums[i]])

        result = []
        getPermutation(sorted(nums), [])
        return result
