# Space : O(n)
# Time  : O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i, v in enumerate(nums):
            if v not in d:
                d[v] = i
            else:
                if i - d[v] <= k:
                    return True
                d[v] = i

        return False
