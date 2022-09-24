from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []

        ans = []
        stack = [[root, [], 0]]

        while stack:
            temp = []
            for node, path, total in stack:
                if not node.left and not node.right:
                    if total + node.val == targetSum:
                        ans.append(path + [node.val])
                if node.left:
                    temp.append(
                        [node.left, path + [node.val], total + node.val])
                if node.right:
                    temp.append(
                        [node.right, path + [node.val], total + node.val])
            stack = temp

        return ans
