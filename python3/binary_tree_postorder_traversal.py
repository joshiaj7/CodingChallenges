"""
Space   : O(1)
Time    : O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getPostorder(self, root: TreeNode) -> List[int]:
        res = []

        if root:
            res += self.getPostorder(root.left)
            res += self.getPostorder(root.right)
            res.append(root.val)

        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.getPostorder(root)
