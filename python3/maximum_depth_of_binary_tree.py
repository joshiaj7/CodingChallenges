from .model import TreeNode

class Solution:
    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = self.getDepth(root.left) + 1
        r = self.getDepth(root.right) + 1

        return max(l, r)

    def maxDepthDFS(self, root: TreeNode) -> int:
        """
        Space   : O(1)
        Time    : O(n)
        """
        return self.getDepth(root)

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        """
        Space   : O(n)
        Time    : O(n)
        """

        if not root:
            return 0
        
        ans = 0
        stack = [root]

        while stack:
            temp = []
            for node in stack:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            ans += 1
            stack = temp

        return ans
