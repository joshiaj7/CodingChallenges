from .model import TreeNode

# Space : O(n) 
# Time  : O(n)

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        ans = []
        stack = [(root, "{}".format(root.val))]
        
        while stack:
            temp = []
            for node, path in stack:
                if node.left:
                    temp.append((node.left, path + "->{}".format(node.left.val)))
                if node.right:
                    temp.append((node.right, path + "->{}".format(node.right.val)))
                if not node.left and not node.right:
                    ans.append(path)
        
            stack = temp
        
        return ans