"""
Space   : O(n)
Time    : O(n)
"""

from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        count = []
        n = len(A)

        for word in A:
            count.append(Counter(word))

        head = count[0]

        for x in range(1, len(A)):
            head = head & count[x]

        for k, v in head.items():
            ans.extend([k] * v)

        return ans
