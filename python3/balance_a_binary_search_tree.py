from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
divide and conquer
"""


class Solution:
    def inorder(self, root):
        res = []

        if root:
            res += self.inorder(root.left)
            res.append(root.val)
            res += self.inorder(root.right)

        return res

    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = self.inorder(root)

        def construct(vals):
            if not vals:
                return None

            mid = len(vals) // 2
            node = TreeNode(vals[mid])
            left = vals[:mid]
            right = vals[mid+1:]

            node.left = construct(left)
            node.right = construct(right)

            return node

        return construct(inorder)
        