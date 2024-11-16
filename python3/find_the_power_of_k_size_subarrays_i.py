from collections import defaultdict
from typing import List

"""
Space   : O(k)
Time    : O(nk)
"""

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)

        window = []
        d = defaultdict(int)

        # init
        for i in range(k):
            window.append(nums[i])
            d[nums[i]] += 1

            if len(window) >= k:
                if self.checkSorted(window, k) and self.checkConsecutive(d, k):
                    ans.append(window[-1])
                else:
                    ans.append(-1)
   
        # calculation
        for i in range(k, n):
            x = nums[i]

            window.append(x)
            d[x] += 1

            popped = window.pop(0)
            if d[popped] - 1 == 0:
                del d[popped] 
            else:
                d[popped] -= 1

            if self.checkSorted(window, k) and self.checkConsecutive(d, k):
                ans.append(x)
            else:
                ans.append(-1)

        return ans

    def checkSorted(self, window, k):
        isSorted = True
        for j in range(1, k):
            if window[j] != window[j-1] + 1 and window[j] != window[j-1]:
                isSorted = False

        return isSorted

    def checkConsecutive(self, d, k):
        isCons = True
        if len(d) != k:
            isCons = False

        return isCons

        