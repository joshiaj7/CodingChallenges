from heapq import heapify, heappop, heappush

"""
Space   : O(n)
Time    : O(n log n)
"""

class SmallestInfiniteSet:

    def __init__(self):
        self.count = 1
        self.mem = set()
        self.heap = []
        heapify(self.heap)

    # Time  : O(log n)        
    def popSmallest(self) -> int:
        if self.heap and self.heap[0] < self.count:
            popped = heappop(self.heap)
            self.mem.remove(popped)
            return popped

        smallest = self.count
        self.count += 1
        return smallest

    # Time  : O(log n)
    def addBack(self, num: int) -> None:
        if num >= self.count or num in self.mem:
            return
        
        self.mem.add(num)
        heappush(self.heap, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
