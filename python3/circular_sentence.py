"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split(" ")
        n = len(arr)

        for i in range(1, n):
            if arr[i][0] != arr[i-1][-1]:
                return False
            
        if arr[0][0] != arr[-1][-1]:
            return False

        return True
