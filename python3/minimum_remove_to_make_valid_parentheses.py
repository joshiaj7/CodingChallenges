"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = list(s)
        indices = []

        for i, c in enumerate(ans):
            if c == "(":
                indices.append(i)
            elif c == ")":
                if indices:
                    indices.pop()
                else:
                    ans[i] = ""

        for j in range(len(indices)):
            ans[indices[j]] = ""

        return "".join(ans)
