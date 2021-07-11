from .model import NaryNode

# Space : O(n)
# Time  : O(n)


class Solution:
    def maxDepth(self, root: NaryNode) -> int:
        if not root:
            return 0

        ans = 0
        stack = [root]

        while stack:
            ans += 1
            temp = []
            for node in stack:
                if node:
                    temp += node.children
            stack = temp

        return ans
