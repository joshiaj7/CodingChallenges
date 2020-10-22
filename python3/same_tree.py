"""
Space   : O(n)
Time    : O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorder(self, root: TreeNode) -> List[int]:
        s = []
        if root:
            s.append(root.val)
            s += self.preorder(root.left)
            s += self.preorder(root.right)
        else:
            return [None]
        return s

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        lp = self.preorder(p)
        lq = self.preorder(q)

        return (lp == lq) and (len(lp) == len(lq))
