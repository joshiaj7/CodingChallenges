from model import TreeNode


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # depth first search
        def dfs(node, paths, curr):
            if node is None:
                return
            if not node.left and not node.right:
                paths.append(curr+str(node.val))
                return
            dfs(node.left, paths, curr+str(node.val))
            dfs(node.right, paths, curr+str(node.val))
            return paths

        ans = 0
        paths = []
        dfs(root, paths, '')
        
        if len(paths) > 0:
            for i in paths:
                ans += int(i, 2)

        return ans
