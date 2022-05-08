from .model import NestedInteger

"""
Space   : O(n)
Time    : O(n)

Method:
DFS
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        def flatten(nested):
            for x in nested:
                if x.isInteger():
                    self.res.append(x.getInteger())
                else:
                    flatten(x.getList())

        self.res = []
        flatten(nestedList)

    def next(self) -> int:
        # if an integer: append, else stop
        return self.res.pop(0)

    def hasNext(self) -> bool:
        return len(self.res) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
