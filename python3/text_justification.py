from typing import List

"""
Space   : O(n)
Time    : O(n * maxWidth)
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans, cur, count = [], [], 0

        for w in words:
            if count + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - count):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                ans.append(''.join(cur))
                cur, count = [], 0
            cur += [w]
            count += len(w)

        return ans + [' '.join(cur).ljust(maxWidth)]
