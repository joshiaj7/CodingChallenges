# leetcode

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        self.isSet = True
        if val not in self.data:
            self.data[val] = 1
        else:
            self.isSet = False
        return self.isSet
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        self.isRemoved = True
        if val in self.data:
            del self.data[val]
        else:
            self.isRemoved = False
        return self.isRemoved
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        self.key, self.val = random.choice(list(self.data.items()))
        print(self.key)
        return self.key
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()