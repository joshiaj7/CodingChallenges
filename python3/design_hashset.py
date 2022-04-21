# Space : O(n)
# Time  : O(1)

class MyHashSet:

    def __init__(self):
        self.hashmap = {}

    def add(self, key: int) -> None:
        self.hashmap[key] = 1

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            del self.hashmap[key]

    def contains(self, key: int) -> bool:
        return key in self.hashmap
