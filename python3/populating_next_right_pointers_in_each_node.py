"""
Space   : O(n)
Time    : O(n)

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        stack = [(root, 0)]

        while stack:
            node, level = stack.pop(0)
            if len(stack) == 0 or stack[0][1] != level:
                node.next = None
            else:
                node.next = stack[0][0]
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))

        return root
