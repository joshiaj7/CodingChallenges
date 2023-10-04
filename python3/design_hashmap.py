"""
Space       : O(n)
Time Put    : O(1)
Time Get    : O(1)
Time Remove : O(1)
"""

class MyHashMap:

    def __init__(self):
        self.arr2D = [[]] * 1024
        
    def put(self, key: int, value: int) -> None:
        key2 = key // 1024
        arr = self.arr2D[key2]
        if not arr:
            arr = [-1] * 1024
            self.arr2D[key2] = arr
        arr[key-key2*1024] = value

    def get(self, key: int) -> int:
        key2 = key // 1024
        arr = self.arr2D[key2]
        if not arr:
            return -1
        return arr[key-key2*1024]

    def remove(self, key: int) -> None:
        key2 = key // 1024
        arr = self.arr2D[key2]
        if not arr:
            return 
        arr[key-key2*1024] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
