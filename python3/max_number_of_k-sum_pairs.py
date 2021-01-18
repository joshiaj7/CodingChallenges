"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        ans = 0

        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

        for key, val in d.items():
            if k - key in d:
                if k - key != key:
                    count = min(val, d[k - key])
                    d[k - key] -= count
                else:
                    count = val // 2
                d[key] -= count
                ans += count

        return ans
