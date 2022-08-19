from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        end = defaultdict(int)

        for x in nums:
            count[x] += 1

        for x in nums:
            if not count[x]:
                continue
            count[x] -= 1
            if end[x-1] > 0:
                end[x-1] -= 1
                end[x] += 1
            elif count[x+1] and count[x+2]:
                count[x+1] -= 1
                count[x+2] -= 1
                end[x+2] += 1
            else:
                return False

        return True
