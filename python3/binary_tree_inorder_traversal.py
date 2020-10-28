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
    def getInorder(self, root: TreeNode) -> List[int]:
        res = []

        if root:
            res += self.getInorder(root.left)
            res.append(root.val)
            res += self.getInorder(root.right)

        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.getInorder(root)
