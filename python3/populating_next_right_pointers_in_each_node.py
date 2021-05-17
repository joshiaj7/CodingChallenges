from .model import BSTNext

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def connect(self, root: BSTNext) -> BSTNext:
        if not root:
            return root

        stack = [(root, 0)]

        while stack:
            node, level = stack.pop(0)
            if len(stack) == 0 or stack[0][1] != level:
                node.next = None
            else:
                node.next = stack[0][0]
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))

        return root
