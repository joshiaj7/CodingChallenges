from bisect import bisect_left
from collections import defaultdict

from bisect import bisect_left

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(dict)
        self.time_list = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[timestamp][key] = value
        self.time_list[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        n = len(self.time_list[key])
        if n == 0:
            return ""
        
        b = bisect_left(self.time_list[key], timestamp)
        # greater than last
        if b == n:
            i = self.time_list[key][-1]
        # unmatched
        elif timestamp != self.time_list[key][b]:
            if b == 0:
                return ""
            else:
                i = self.time_list[key][b-1]
        # matched
        else:
            i = self.time_list[key][b]

        return self.hashmap[i][key]

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
