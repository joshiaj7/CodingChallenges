from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

        return root
