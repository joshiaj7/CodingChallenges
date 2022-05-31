"""
space : O(n)
time  : O(n)

Method:
Sliding window
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        checklist = set()
        n = len(s)

        for i in range(n-k+1):
            checklist.add(s[i:i+k])

        return len(checklist) == 2 ** k
