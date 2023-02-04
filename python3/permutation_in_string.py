"""
Space   : O(n1)
Time    : O(n1 + n2 * n1)
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        if len(s1) > len(s2):
            return False

        n1, n2 = len(s1), len(s2)

        for c in s1:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        # sliding window
        check = {}
        for i in range(n1):
            if s2[i] in check:
                check[s2[i]] += 1
            else:
                check[s2[i]] = 1

        if check == d:
            return True

        for j in range(n1, n2):
            i = j-n1

            # addition
            if s2[j] in check:
                check[s2[j]] += 1
            else:
                check[s2[j]] = 1

            # subtraction
            if check[s2[i]] > 1:
                check[s2[i]] -= 1
            else:
                del check[s2[i]]

            if check == d:
                return True

        return False
