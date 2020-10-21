"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for e in asteroids:
            if not stack or stack[-1] < 0 or e > 0:
                stack.append(e)

            else:
                flag = True
                while stack and stack[-1] > 0 and stack[-1] <= -e:
                    tmp = stack.pop()
                    if tmp == -e:
                        flag = False
                        break
                if (not stack or stack[-1] < 0) and flag:
                    stack.append(e)
        return stack
