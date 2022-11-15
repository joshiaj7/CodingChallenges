from .model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            return dfs(root.left) + dfs(root.right) + 1
            
        return dfs(root)
