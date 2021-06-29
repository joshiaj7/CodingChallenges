# Space : O(1)
# Time  : O(n)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones, zeros, start = 0, 0, 0
        n, ans = len(nums), 0

        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1

            while zeros > k:
                if nums[start] == 1:
                    ones -= 1
                else:
                    zeros -= 1
                start += 1

            ans = max(ans, i - start + 1)

        return ans
