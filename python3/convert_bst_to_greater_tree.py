from model import TreeNode

# Space : O(n)
# Time  : O(n)

class Solution:
    def getInorder(self, root: TreeNode) -> List[int]:
        res = []
        
        if root:
            res += self.getInorder(root.left)
            res.append(root.val)
            res += self.getInorder(root.right)
            
        return res
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        def insertGreaterTree(point, nodes):
            if nodes and point:
                insertGreaterTree(point.left, nodes)
                point.val = nodes.pop(0)
                insertGreaterTree(point.right, nodes)
        
        nodes = self.getInorder(root)
        for i in range(len(nodes)-2,-1,-1):
            nodes[i] += nodes[i+1]
        
        p = root
        insertGreaterTree(p, nodes)
        
        return root