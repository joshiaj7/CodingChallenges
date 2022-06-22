"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    # O(N) Time, worth to consider
    # but still slower than sorted
    def findKthLargestPartition(self, nums: List[int], k: int) -> int:
        return self.findKthSmallest(nums, len(nums)+1-k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
