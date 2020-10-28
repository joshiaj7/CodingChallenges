"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        n = len(nums)
        if n == 1:
            return [str(nums[0])]

        ans = []
        s, e = '', ''
        for i in range(n):
            if i == 0:
                s = nums[i]
                continue
            if nums[i] - nums[i-1] == 1:
                e = nums[i]
                continue
            elif nums[i] - nums[i-1] > 1:
                if e == '':
                    ans.append("{}".format(s))
                else:
                    ans.append("{}->{}".format(s, e))
                s = nums[i]
                e = ''

        if e == '':
            ans.append("{}".format(s))
        else:
            ans.append("{}->{}".format(s, e))

        return ans
