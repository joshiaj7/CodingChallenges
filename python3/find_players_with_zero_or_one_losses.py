"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]
        lose = {}
        players = set()

        for w, l in matches:
            if l in lose:
                lose[l] += 1
            else:
                lose[l] = 1

            players.add(w)
            players.add(l)

        players = sorted(list(players))
        for p in players:
            if p not in lose:
                ans[0].append(p)
            elif lose[p] == 1:
                ans[1].append(p)

        return ans
