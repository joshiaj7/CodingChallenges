"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_range, total_nums = sum([i for i in range(1, n+1)]), sum(nums)

        double = total_nums - sum(set(nums))

        return [double, total_range - total_nums + double]
