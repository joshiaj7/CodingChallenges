from typing import List

"""
Space   : O(3^n)
Time    : O(3^n)
"""

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        return self.bt(stones, 1, 1, target)

    def bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur == target:
            return True
        
        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False
        
        # dfs
        candidate = [speed-1, speed, speed+1]
        for c in candidate:
            if (cur + c) in stones:
                if self.bt(stones, cur+c, c, target):
                    return True

        self.memo.add((cur,speed))
        return False
