from .model import QuadTree

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

Space   : O(n)
Time    : O(n)
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> QuadTree:

        if not grid: 
            return None

        if self.isLeaf(grid):
            return QuadTree(grid[0][0] == 1, True, None, None, None, None)

        n = len(grid)
        return QuadTree('*',
                    False,
                    self.construct([row[:n//2] for row in grid[:n//2]]),
                    self.construct([row[n//2:] for row in grid[:n//2]]),
                    self.construct([row[:n//2] for row in grid[n//2:]]),
                    self.construct([row[n//2:] for row in grid[n//2:]]))

    def isLeaf(self, grid):
        return all(grid[i][j] == grid[0][0] 
            for i in range(len(grid)) for j in range(len(grid[i])))
