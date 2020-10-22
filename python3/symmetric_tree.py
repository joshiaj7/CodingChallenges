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
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True

        if root.left and root.right:
            stack = [(root.left, "l"), (root.right, "r")]
        else:
            return False

        while stack:
            if len(stack) % 2 == 1:
                return False

            l = stack.pop(0)
            r = stack.pop()

            if l[0].val != r[0].val or l[1] == r[1]:
                return False
            if l[0].right:
                stack.insert(0, (l[0].right, "r"))
            if l[0].left:
                stack.insert(0, (l[0].left, "l"))
            if r[0].left:
                stack.append((r[0].left, "l"))
            if r[0].right:
                stack.append((r[0].right, "r"))

        return True
