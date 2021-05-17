from .model import TreeNode


class Solution:
    def getPreorder(self, root: TreeNode, low: int, high: int) -> List[int]:
        res = []
        
        if root:
            if low <= root.val <= high:
                res.append(root.val)
            res += self.getPreorder(root.left, low, high)
            res += self.getPreorder(root.right, low, high)
            
        return res
    
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """
        Personal attempt
        Space   : O(n)
        Time    : O(n)
        """
        def insertNode(val, node):
            if val < node.val:
                if node.left:
                    insertNode(val, node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    insertNode(val, node.right)
                else:
                    node.right = TreeNode(val)
        
        nodes = self.getPreorder(root, low, high)
        if not nodes:
            return None
        
        ans = TreeNode(nodes[0])
        for i in range(1, len(nodes)):
            insertNode(nodes[i], ans)
        
        return ans

    def trimBSTBest(self, root, low, high):
        """
        Best Solution
        Space   : O(1)
        Time    : O(n)
        """
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)