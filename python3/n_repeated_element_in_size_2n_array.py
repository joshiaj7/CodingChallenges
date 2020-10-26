"""
Space    : O(n)
Time     : O(n)
"""


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        nums = set()
        for i in A:
            if i in nums:
                return i
            else:
                nums.add(i)
