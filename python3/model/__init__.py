class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class BSTNext:
    def __init__(self, val: int = 0, left: BSTNext = None, right: BSTNext = None, next: BSTNext = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class RandListNode:
    def __init__(self, x: int, next: RandListNode = None, random: RandListNode = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True

    def search(self, word):
        p = self.root
        for i, c in enumerate(word):
            if c not in p:
                return word
            p = p[c]
            if '#' in p:
                return word[:i+1]
        return word

    def starts(self, prefix):
        t = self.root
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True

    def remove(self, word):
        t = self.root
        nodes = []
        for w in word:
            if w not in t:
                return False
            t = t[w]
            nodes.append((t, w))

        if '#' in t:
            p = '#'
            for n, w in nodes[::-1]:
                if len(n[p]) == 0 or p == '#':
                    del n[p]
                p = w


class NaryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class NestedInteger:
    def isInteger(self) -> bool:
        return True
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

    def getInteger(self) -> int:
        return 0
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

    def getList(self) -> List[NestedInteger]:
        return NestedInteger()
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


# Definition for a QuadTree node.
class QuadTree:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# Definition for a Node.
class GraphNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Definition for a Mountain Array.

class MountainArray:
    def __init__(self):
        self.arr = []

    def get(self, index: int) -> int:
       return self.arr[index]

    def length(self) -> int:
        return len(self.arr)
