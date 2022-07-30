from collections import Counter

"""
Space   : O(n)
Time    : O(n + m)
"""


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = Counter()
        for w in words2:
            count |= Counter(w)

        ans = []
        for w in words1:
            if not (count - Counter(w)):
                ans.append(w)
        return ans
