from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        stack = [root]

        level = 2
        while stack:
            temp = []
            for node in stack:
                if level == depth:
                    left = node.left
                    right = node.right
                    node.left = TreeNode(val)
                    node.left.left = left
                    node.right = TreeNode(val)
                    node.right.right = right

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            if level == depth:
                break
            stack = temp
            level += 1

        return root
