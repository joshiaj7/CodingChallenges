from typing import List, Optional
from model import TreeNode

"""
Space   : O(2^n)
Time    : O(n * 2^n)
"""


class Solution:
    def clone(self, tree: TreeNode) -> TreeNode:
        if not tree:
            return None
        new_tree = TreeNode(0)
        new_tree.left = self.clone(tree.left)
        new_tree.right = self.clone(tree.right)
        return new_tree

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]
        
        ans = []
        for i in range(2, n + 1, 2):
            left_branch = self.allPossibleFBT(i - 1)
            right_branch = self.allPossibleFBT(n - i)
            for left_count, left in enumerate(left_branch, 1):
                for right_count, right in enumerate(right_branch, 1):
                    tree = TreeNode(0)

                    tree.left = self.clone(left) if right_count < len(right_branch) else left
                    tree.right = self.clone(right) if left_count < len(left_branch) else right

                    ans.append(tree)
        return ans
