class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        if x > y:
            top = "ab"
            topv = x
            bot = "ba"
            botv = y
        else:
            top = "ba"
            topv = y
            bot = "ab"
            botv = x

        stack = []
        for l in s:
            if l == top[1] and stack and stack[-1] == top[0]:
                ans += topv
                stack.pop()
            else:
                stack.append(l)

        new_stack = []
        for l in stack:
            if l == bot[1] and new_stack and new_stack[-1] == bot[0]:
                ans += botv
                new_stack.pop()
            else:
                new_stack.append(l)

        return ans

        