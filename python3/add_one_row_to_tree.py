from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            ans = TreeNode(v)
            ans.left = root
            return ans

        level = 1
        stack = [root]

        while stack:
            temp = []
            if level + 1 == d:
                for node in stack:
                    if node.left:
                        l = node.left
                        node.left = TreeNode(v)
                        node.left.left = l
                    else:
                        node.left = TreeNode(v)
                    if node.right:
                        r = node.right
                        node.right = TreeNode(v)
                        node.right.right = r
                    else:
                        node.right = TreeNode(v)
                break

            for node in stack:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            stack = temp
            level += 1

        return root
