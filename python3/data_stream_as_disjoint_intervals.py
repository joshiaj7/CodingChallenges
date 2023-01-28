"""
Space   : O(n)
Time    : O(n log n)

Union find
"""


class SummaryRanges:

    def __init__(self):
        self.p = {}
        self.interval = {}
        
    def makeSet(self, x):
        self.p[x] = x
        self.interval[x] = [x, x]

    def find(self, x):
        if x not in self.p:
            return None

        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX is None or rootY is None:
            return

        self.p[rootX] = rootY

        x_interval = self.interval[rootX]
        del self.interval[rootX]

        self.interval[rootY] = [min(self.interval[rootY][0], x_interval[0]), max(self.interval[rootY][1], x_interval[1])]


    def addNum(self, value: int) -> None:
        if value in self.p:
            return

        self.makeSet(value)

        self.union(value, value-1)
        self.union(value, value+1)


    def getIntervals(self) -> List[List[int]]:
        return sorted(self.interval.values())


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
