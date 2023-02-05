"""
Space   : O(np)
Time    : O(np + ns * np)
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        d = {}
        ns, np = len(s), len(p)

        if np > ns:
            return []

        for c in p:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        # sliding window
        check = {}
        for i in range(np):
            if s[i] in check:
                check[s[i]] += 1
            else:
                check[s[i]] = 1

        if check == d:
            ans.append(0)

        for j in range(np, ns):
            i = j-np

            # addition
            if s[j] in check:
                check[s[j]] += 1
            else:
                check[s[j]] = 1

            # subtraction
            if check[s[i]] > 1:
                check[s[i]] -= 1
            else:
                del check[s[i]]

            if check == d:
                ans.append(i+1)

        return ans
