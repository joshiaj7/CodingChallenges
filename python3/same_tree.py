from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""



class Solution:
    def preorder(self, root: TreeNode) -> List[int]:
        s = []
        if root:
            s.append(root.val)
            s += self.preorder(root.left)
            s += self.preorder(root.right)
        else:
            return [None]
        return s

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        lp = self.preorder(p)
        lq = self.preorder(q)

        return (lp == lq) and (len(lp) == len(lq))
