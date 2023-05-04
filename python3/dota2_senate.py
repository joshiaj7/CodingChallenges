"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = []
        signs = [0, 0]
        bans = [0, 0]

        for s in senate:
            x = s == "R"
            signs[x] += 1
            queue.append(x)

        while all(signs):
            x = queue.pop(0)
            signs[x] -= 1
            if bans[x] > 0:
                bans[x] -= 1
            else:
                bans[x^1] += 1
                queue.append(x)
                signs[x] += 1

        return "Radiant" if signs[1] else "Dire"
