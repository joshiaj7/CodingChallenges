# leetcode

class MinStack:    
    def __init__(self):
        self.item = []
    
    def push(self, x: int) -> None:
        self.item.append(x)

    def pop(self) -> None:
        self.item.pop()
        
    def top(self) -> int:
        return self.item[-1]        

    def getMin(self) -> int:
        min_val = 100000000000000000000
        for i in self.item:
            min_val = min(min_val, i)
        return min_val        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()