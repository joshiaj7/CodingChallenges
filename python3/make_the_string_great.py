"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if not stack:
                stack.append(c)
                continue

            if stack[-1] != c and stack[-1].lower() == c.lower():
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
