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
    def getPreorder(self, root: TreeNode) -> List[int]:
        res = []

        if root:
            res.append(root.val)
            res += self.getPreorder(root.left)
            res += self.getPreorder(root.right)

        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.getPreorder(root)
