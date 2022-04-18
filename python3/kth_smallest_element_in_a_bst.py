from .model import TreeNode

# Space   : O(n)
# Time    : O(n)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            res = []

            if root:
                res += inorder(root.left)
                res.append(root.val)
                res += inorder(root.right)

            return res

        return inorder(root)[k-1]
