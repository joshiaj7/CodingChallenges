"""
Space   : O(1)
Time    : O(log n)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        s, e = 0, len(nums)-1

        while s <= e:
            mid = (s+e) // 2
            if nums[mid] == target:
                return True

            # check left
            if nums[s] < nums[mid]:
                if nums[s] <= target < nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            elif nums[s] == nums[mid]:
                s += 1
            # check right
            else:
                if nums[mid] < target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1

        return False
