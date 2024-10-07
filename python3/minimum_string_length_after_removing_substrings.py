"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            stack.append(c)
            
            while stack and len(stack) > 1:
                if stack[-2] == "A" and stack[-1] == "B":
                    stack = stack[:-2]
                elif stack[-2] == "C" and stack[-1] == "D":
                    stack = stack[:-2]
                else:
                    break

        return len(stack)
        