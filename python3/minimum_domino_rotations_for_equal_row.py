"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ansTop, ansBot = 0, 0
        revTop, revBot = 0, 0
        n = len(A)

        top, bot = A[0], B[0]
        chainA, chainB = True, True

        for i in range(1, n):
            if chainA:
                if A[i] == top or B[i] == top:
                    chainA = True
                else:
                    chainA = False

            if chainB:
                if A[i] == bot or B[i] == bot:
                    chainB = True
                else:
                    chainB = False

            if not chainA and not chainB:
                return -1

        if chainA or chainB:
            for j in range(n):
                if chainA:
                    # check top
                    if A[j] != top:
                        ansTop += 1
                    # check bot
                    if B[j] != top:
                        revTop += 1

                if chainB:
                    # check top
                    if A[j] != bot:
                        ansBot += 1
                    # check bot
                    if B[j] != bot:
                        revBot += 1

        if chainA and chainB:
            return min(ansTop, ansBot, revTop, revBot)
        elif chainA:
            return min(ansTop, revTop)
        elif chainB:
            return min(ansBot, revBot)

        return -1
