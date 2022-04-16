from .model import TreeNode

# Space : O(1)
# Time  : O(n)


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def convert(root, total):
            if not root:
                return total

            total = convert(root.right, total)
            root.val += total
            total = convert(root.left, root.val)

            return total

        convert(root, 0)
        return root
