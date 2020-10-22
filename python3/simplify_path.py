"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        i = 0

        while i < len(paths):
            if paths[i] == '' or paths[i] == '.':
                del paths[i]
            else:
                i += 1

        stack = []
        for i in paths:
            if i == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)
