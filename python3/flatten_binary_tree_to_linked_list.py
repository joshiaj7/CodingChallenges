from .model import TreeNode

# Space : O(n)
# Time  : O(n)

class Solution:
    def getInorder(self, root: TreeNode) -> List[int]:
        res = []

        if root:
            res.append(root.val)
            res += self.getInorder(root.left)
            res += self.getInorder(root.right)

        return res

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        vals = self.getInorder(root)
        print(vals)

        head = root

        i = 0
        while i < len(vals):
            if i < len(vals)-1:
                head.val = vals[i]
                head.left = None
                head.right = TreeNode(i)
                head = head.right
            else:
                head.val = vals[i]
            i += 1
