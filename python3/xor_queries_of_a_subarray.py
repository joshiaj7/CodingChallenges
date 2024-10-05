from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(arr)
        prefix = []

        for i in range(n):
            if i == 0:
                prefix.append(arr[i])
            else:
                prefix.append(arr[i] ^ prefix[-1])

        for l, r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[l-1] ^ prefix[r])

        return ans
