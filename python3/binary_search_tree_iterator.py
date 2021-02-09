from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.mem = self.getInorder(root)

    def getInorder(self, root: TreeNode) -> List[int]:
        vals = []

        if root:
            vals += self.getInorder(root.left)
            vals.append(root.val)
            vals += self.getInorder(root.right)

        return vals

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.mem.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.mem) > 0:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
