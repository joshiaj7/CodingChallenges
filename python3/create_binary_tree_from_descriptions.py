from typing import List, Optional
from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = {}
        children = set()
        parents = set()

        for parent, child, isLeft in descriptions:
            pnode = None
            if parent in nodeMap:
                pnode = nodeMap[parent]
            else:
                pnode = TreeNode(parent)
                nodeMap[parent] = pnode

            cnode = None
            if child in nodeMap:
                cnode = nodeMap[child]
            else:
                cnode = TreeNode(child)
                nodeMap[child] = cnode
                
            if isLeft:
                pnode.left = cnode
            else:
                pnode.right = cnode

            parents.add(parent)
            children.add(child)

        root = 0
        for p in list(parents):
            if p not in children:
                root = p
                break

    
        return nodeMap[root]
        