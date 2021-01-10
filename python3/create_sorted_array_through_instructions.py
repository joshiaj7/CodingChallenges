from sortedcontainers import SortedList

"""
O(log(n)) -> Bisect method works on the concept of binary search
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        answer = 0
        instructionsSorted = SortedList()
        for instruction in instructions:
            left = instructionsSorted.bisect_left(instruction)
            right = len(instructionsSorted) - \
                instructionsSorted.bisect(instruction)
            answer += left if left < right else right
            instructionsSorted.add(instruction)
        return answer % (10**9 + 7)
