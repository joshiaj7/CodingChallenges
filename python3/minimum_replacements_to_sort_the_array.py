"""
Space   : O(1)
Time    : O(n)

Google interview question
"""

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1] # current biggest number
        n = len(nums)
        ans = 0

        """
        initial 
        nums = [2, 10, 5]
        x = 5

        1st iter
        cur = 5
        k = (5 + 5 - 1) // 5 = 1
        x = 5 // 1 = 5
        ans += 1 - 1 = 0

        2nd iter
        cur = 10
        k = (10 + 5 - 1) // 5 = 2
        x = 10 // 2 = 5
        ans += 2 - 1 = 1

        3rd iter
        cur = 2
        k = (2 + 5 - 1) // 5 = 1
        x = 2 // 1 = 2
        ans += 1 - 1 = 1
        """

        for i in range(n -1, -1, -1):
            # ceiling division
            k = (nums[i] + last - 1) // last

            # use ceiling division to get the smallest number
            # and store it in x
            last= nums[i] // k

            # add answer - 1
            ans += k - 1
            
        return ans
