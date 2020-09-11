class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 10**10 * -1
        leng = len(nums)

        count1 = 1
        count2 = 1
        for idx in range(leng):
            # front
            count1 *= nums[idx]
            ans = max(ans, count1)
            if count1 == 0:
                count1 = max(count1, 1)

            # back
            count2 *= nums[leng - 1 - idx]
            ans = max(ans, count2)
            if count2 == 0:
                count2 = max(count2, 1)

        return ans
