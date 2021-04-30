# Space   : O(1)
# Time    : O(log n)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        s, e = 0, len(nums)-1
        
        if not nums:
            return ans

        while s < e:
            m = (s + e) // 2
            if nums[m] < target:
                s = m + 1
            else:
                e = m

        if nums[e] != target:
            return [-1, -1]
        ans[0] = e
        
        e = len(nums)-1
        while s < e:
            m = ((s + e) // 2)+1
            if nums[m] <= target:
                s = m
            else:
                e = m - 1
        
        ans[1] = e
        
        return ans