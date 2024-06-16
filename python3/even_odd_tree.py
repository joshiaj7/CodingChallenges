from typing import Optional
from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        level = 0

        while stack:
            temp = []

            prevVal = 0
            for i, node in enumerate(stack):
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False

                    if i == 0:  
                        prevVal = node.val
                    else:
                        if node.val <= prevVal:
                            return False
                        prevVal = node.val
                else:
                    if node.val % 2 == 1:
                        return False

                    if i == 0:  

                        prevVal = node.val
                    else:
                        if node.val >= prevVal:
                            return False
                        prevVal = node.val

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            level += 1
            stack = temp


        return True
        