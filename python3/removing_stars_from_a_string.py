"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "*" and len(stack) > 0:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
