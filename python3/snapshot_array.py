from bisect import bisect

"""
Space   : O(S)
Time    : O(log(S))
S = number of snapshots
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[-1,0]] for _ in range(length)]
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.arr[index], [snap_id + 1]) - 1
        return self.arr[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
