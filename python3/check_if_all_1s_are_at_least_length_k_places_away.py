"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        cur = -1
        for i in range(n):
            if nums[i] == 1:
                if cur == -1:
                    cur = i
                    continue

                if i - cur - 1 >= k:
                    cur = i
                else:
                    return False

        return True
