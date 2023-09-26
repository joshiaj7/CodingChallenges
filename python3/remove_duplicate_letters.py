"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []
        last_char_idx = {}
        visited = set()

        for i in range(n):
            last_char_idx[s[i]] = i

        for i, c in enumerate(s):
            if c not in visited:
                while stack and stack[-1] > c and last_char_idx[stack[-1]] > i:
                    visited.remove(stack.pop())

                stack.append(c)
                visited.add(c)

        return "".join(stack)
