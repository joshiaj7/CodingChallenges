"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []

        for i in range(n):
            if not stack:
                stack.append(s[i])
                continue

            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True
