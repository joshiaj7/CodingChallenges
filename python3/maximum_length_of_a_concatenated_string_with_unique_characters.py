"""
Space   : O(n^2)
Time    : O(n^2)
"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for s in arr:
            # check duplicate char
            if len(set(s)) < len(s):
                continue

            # cast to set
            s = set(s)

            # compare with strings in dp
            for t in dp[:]:
                # has to be false / 0
                if s & t:
                    continue
                dp.append(s | t)

        return max(len(s) for s in dp)
