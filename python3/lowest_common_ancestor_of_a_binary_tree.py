from .model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root in [None, p, q]:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        return root if left and right else left or right
            

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []

        def getPath(root, path, node):
            if not root:
                return False

            path.append(root)

            if root.val == node.val:
                return True

            left = root.left and getPath(root.left, path, node)
            right = root.right and getPath(root.right, path, node)

            if left or right:
                return True

            path.pop()
            return False

        getPath(root, path1, p)
        getPath(root, path2, q)

        d = {}
        for node in path1:
            d[node.val] = node

        ans = None
        for node in path2:
            if node.val in d:
                ans = node
            else:
                break

        return ans


        