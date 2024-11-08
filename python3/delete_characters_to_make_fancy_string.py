"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for l in s:
            stack.append(l)
            if len(stack) >= 3 and stack[-1] == stack[-2] ==  stack[-3] == l:
                stack.pop()

        return "".join(stack)
