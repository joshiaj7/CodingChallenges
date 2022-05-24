from collections import OrderedDict

# using double linked list
# Space : O(n)
# Time  : O(1)


class LRUNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCacheLL:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = LRUNode(0, 0)
        self.tail = LRUNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = LRUNode(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# using OrderedDict
# Space : O(n)
# Time  : O(1)


class LRUCacheOrdDict:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        v = self.cache[key]
        del self.cache[key]
        self.cache[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
