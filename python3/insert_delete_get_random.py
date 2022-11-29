import random

"""
Space   : O(n)
Time    : O(1)
"""

class RandomizedSet:

    def __init__(self):
        self.data = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data[val] = 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        del self.data[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(list(self.data.keys()))
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
