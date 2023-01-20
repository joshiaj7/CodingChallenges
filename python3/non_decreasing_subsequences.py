"""
Space   : O(2^n)
Time    : O(2^n)

backtracking
"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(index):
            if len(path) > 1:
                ans.append(path[:])
            for i in range(index, len(nums)):
                if path and path[-1] > nums[i]:
                    continue
                if i > index and nums[i] in nums[index:i]:
                    continue
                path.append(nums[i])
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return ans
