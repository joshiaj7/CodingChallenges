"""
Space   : O(1)
Time    : O(log n)
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# dummy guess
def guess(num: int) -> int:
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 0, n

        while low <= high:
            mid = (low + high) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                low = mid + 1
            else:
                high = mid - 1
        
        return 0

    