from .model import TreeNode

"""
Space : O(1)
Time  : O(n)

Mehtod:
DFS
"""

class Solution:
    ans = 0
    def minCameraCover(self, root: TreeNode) -> int:
        """
        0 : None node
        1 : Supervised
        2 : Supervised 2x
        3 : Leaf / Unsupervised node
        """
        def dfs(node: TreeNode) -> int:
            if not node: 
                return 0
            val = dfs(node.left) + dfs(node.right)
            if val == 0: 
                return 3
            if val < 3: 
                return 0
            self.ans += 1
            return 1
        return self.ans + 1 if dfs(root) > 2 else self.ans
