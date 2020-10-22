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
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if not root:
            return []

        sums = []
        stack = [(root, [])]

        while stack:
            node, mem = stack.pop()
            if not node.left and not node.right:
                sums.append(mem + [node.val])
            if node.left:
                stack.append((node.left, mem + [node.val]))
            if node.right:
                stack.append((node.right, mem + [node.val]))

        ans = []
        for item in sums:
            if sum(item) == s:
                ans.append(item)

        return ans
