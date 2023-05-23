from typing import List

"""
Space   : O(n)
Time    : O(n log n + n ^ 3)
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(l, r, n, target, path):
            if r - l + 1 < n or n < 2 or nums[l] * n > target or nums[r] * n < target:
                return
            
            if n == 2:
                while l < r:
                    curr_sum = nums[l] + nums[r]
                    if curr_sum > target:
                        r -= 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        ans.append(path + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                return
            else:
                for i in range(l, r+1):
                    if i > l and nums[i] == nums[i - 1]:
                        continue
                    dfs(i + 1, r, n - 1, target - nums[i], path + [nums[i]])

        nums.sort()
        dfs(0, len(nums) - 1, 4, target, [])

        return ans
