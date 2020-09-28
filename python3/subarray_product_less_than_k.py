class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j, ans = 0, -1, 0
        N = len(nums)

        prod = 1
        while j < N-1:
            j += 1
            prod *= nums[j]
            if prod < k:
                ans += (j - i + 1)
            else:
                while (i <= j and prod >= k):
                    prod //= nums[i]
                    i += 1
                if i <= j:
                    ans += (j - i + 1)

        return ans
