# Space : O(1)
# Time  : O(n)

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, bucket1, bucket2 = 0, 0, 0

        for x in nums:
            bucket1 = bucket1 + 1 if x < left else 0
            bucket2 = bucket2 + 1 if x <= right else 0
            ans += bucket2 - bucket1

        return ans
