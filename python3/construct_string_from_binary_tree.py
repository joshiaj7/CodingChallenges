from .model import TreeNode

# Space : O(1)
# Time  : O(n)


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        s = ""

        if root:
            s += str(root.val)
            if root.left:
                s += "(" + self.tree2str(root.left) + ")"
            if not root.left and root.right:
                s += "()"
            if root.right:
                s += "(" + self.tree2str(root.right) + ")"

        return s
