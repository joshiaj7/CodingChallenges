"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def calculate(self, s: str) -> int:
        ans, num, sign, stack = 0, 0, 1, []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+" or c == "-":
                ans += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(ans)
                stack.append(sign)
                sign, ans = 1, 0
            elif c == ")":
                ans += sign * num
                ans *= stack.pop()
                ans += stack.pop()
                num = 0

        return ans + sign * num
