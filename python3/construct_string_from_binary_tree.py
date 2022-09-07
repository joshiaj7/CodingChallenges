from .model import TreeNode

# Space : O(1)
# Time  : O(n)


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""

        l, r = "", ""
        left = self.tree2str(root.left)
        if left:
            l = "({})".format(left)

        right = self.tree2str(root.right)
        if right:
            r = "({})".format(right)

        if not l and r:
            l = "()"

        return str(root.val) + l + r



            
