"""
Space   : O(n)
Time    : O(n^2)
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 0
        dif = 10000

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while(j < k):
                s = nums[i] + nums[j] + nums[k]
                if(abs(s-target) <= dif):
                    dif = abs(s - target)
                    ans = s

                if(s < target):
                    j += 1
                else:
                    k -= 1

        return ans
