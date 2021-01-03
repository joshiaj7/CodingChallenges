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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        stack = [root]

        while stack:
            temp = []
            l = []
            for x in stack:
                l.append(x.val)
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            ans.insert(0, l)
            stack = temp

        return ans
