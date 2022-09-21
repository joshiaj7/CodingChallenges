"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        m = len(queries)
        ans = []
        total = 0

        for num in nums:
            if num % 2 == 0:
                total += num

        for val, idx in queries:
            # all even
            if nums[idx] % 2 == 0 and val % 2 == 0:
                total += val
            # all odd
            if nums[idx] % 2 != 0 and val % 2 != 0:
                total += nums[idx] + val
            # val is odd
            if nums[idx] % 2 == 0 and val % 2 != 0:
                total -= nums[idx]

            nums[idx] += val
            ans.append(total)

        return ans
