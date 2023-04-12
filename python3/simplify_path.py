"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splitted_path = path.split("/")

        for directory in splitted_path:
            if directory == "" or directory == ".":
                continue

            if directory == "..": 
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(directory)

        return "/" + "/".join(stack)
