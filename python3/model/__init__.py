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


class NaryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
