"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A, B = 0, 0
        n = len(colors)

        for i in range(1, n-1):
            if colors[i] == colors[i-1] and colors[i] == colors[i+1]:
                if colors[i] == "A":
                    A += 1
                else:
                    B += 1
        

        return A > B
        