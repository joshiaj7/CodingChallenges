from .model import TreeNode

"""
BFS Solution
Space   : O(n)
Time    : O(K + H), K = 9, H = Height
"""


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode, count=0) -> int:
        if not root:
            return 0
        count ^= 1 << (root.val - 1)
        res = self.pseudoPalindromicPaths(
            root.left, count) + self.pseudoPalindromicPaths(root.right, count)
        if root.left == root.right:
            if count & (count - 1) == 0:
                res += 1
        return res
