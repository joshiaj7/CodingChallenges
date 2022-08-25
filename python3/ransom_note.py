from collections import Counter

"""
Space : O(n)
Time  : O(n)
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return len(Counter(ransomNote) - Counter(magazine)) == 0
