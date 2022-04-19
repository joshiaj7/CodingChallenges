from .model import TreeNode

# Space   : O(1)
# Time    : O(n)


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        prev, first, second = None, None, None

        def swap(root):
            if root:
                swap(root.left)
                nonlocal prev, first, second

                if prev and root.val < prev.val:
                    if not first:
                        first = prev
                    second = root
                prev = root
                swap(root.right)

        swap(root)
        first.val, second.val = second.val, first.val
