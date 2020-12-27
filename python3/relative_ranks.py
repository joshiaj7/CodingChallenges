"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if not nums:
            return []

        if n > 3:
            s = sorted(nums)
            d = {}
            for i in range(n):
                if i < n-3:
                    d[s[i]] = str(n - i)
                elif i == n-3:
                    d[s[i]] = "Bronze Medal"
                elif i == n-2:
                    d[s[i]] = "Silver Medal"
                elif i == n-1:
                    d[s[i]] = "Gold Medal"

            for j in range(n):
                nums[j] = d[nums[j]]

            return nums

        w1, w2, w3 = 0, 0, 0
        for i in range(n):
            if nums[i] > w1:
                w3 = w2
                w2 = w1
                w1 = nums[i]
            elif nums[i] > w2:
                w3 = w2
                w2 = nums[i]
            elif nums[i] > w3:
                w3 = nums[i]

        for j in range(n):
            if nums[j] == w1:
                nums[j] = "Gold Medal"
            elif nums[j] == w2:
                nums[j] = "Silver Medal"
            elif nums[j] == w3:
                nums[j] = "Bronze Medal"

        return nums
