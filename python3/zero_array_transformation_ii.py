from typing import List

"""
Space   : O(n)
Time    : O(n log k)
binary search
"""

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        k = len(queries)

        left = 0
        right = k - 1
        ans = -1

        if sum(nums) == 0:
            return 0

        while left <= right:
            mid = (left + right) // 2

            diffArr = [0 for _ in range(n+1)]

            for i in range(mid+1):
                l, r, val = queries[i]
                diffArr[l] += val
                diffArr[r+1] -= val

            for i in range(1, n+1):
                diffArr[i] = diffArr[i] + diffArr[i-1]

            fulfilled = True
            for i in range(n):
                if nums[i] > diffArr[i]:
                    fulfilled = False
                    break

            if not fulfilled:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid + 1

        return ans
        