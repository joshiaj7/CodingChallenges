"""
space   : O(n)
time    : O(n log n)
"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        temp = []
        nums = sorted(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] == k:
                    if (nums[i], nums[j]) not in temp:
                        temp.append((nums[i], nums[j]))
                        ans += 1
                elif nums[j] - nums[i] > k:
                    break

        return ans
