from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return[]

        mem = []

        stack = [root]

        while stack:
            node = stack.pop()
            mem.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        hashmap = {}
        max_count = 0

        for i in mem:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
            max_count = max(max_count, hashmap[i])

        mode = []
        for k, v in hashmap.items():
            if v == max_count:
                mode.append(k)

        return mode
