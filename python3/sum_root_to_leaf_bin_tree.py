# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
        print(paths)

        if len(paths) > 0:
            for i in paths:
                ans += int(i, 2)

        return ans
