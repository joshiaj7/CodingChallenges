"""
Space   : O(n)
Time    : O(n)

Method:
Stack
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        ans = ""

        for x in s:
            if len(stack) == 0:
                stack.append([x, 1])
            elif stack[-1][0] == x:
                stack[-1][1] += 1
            else:
                stack.append([x, 1])
            ans += x

            if stack[-1][1] == k:
                ans = ans[:len(ans)-k]
                stack.pop()

        return ans
