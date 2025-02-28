from collections import defaultdict
from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = 0

        nums.sort(key=lambda x: -x)
        sumArr = []
        for num in nums:
            s = str(num)

            total = 0
            for c in s:
                total += int(c)

            sumArr.append(total)

        h = defaultdict(list)
        for i, v in enumerate(sumArr):
            h[v].append(i)

        for _, v in h.items():
            l = len(v)
            if l > 1:
                ans = max(ans, nums[v[0]] + nums[v[1]])
    
        return ans if ans > 0 else -1
        