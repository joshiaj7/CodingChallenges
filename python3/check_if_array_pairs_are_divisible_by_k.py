from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = {}
        for x in arr:
            mod = x % k
            if mod not in d:
                d[mod] = 1
            else:
                d[mod] += 1

        for key, val in d.items():
            if key == 0:
                if val % 2 != 0:
                    return False
                else:
                    continue

            pair = k - key
            if pair not in d:
                return False

            if val != d[pair]:
                return False

        return True

        