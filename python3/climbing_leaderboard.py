"""
Space   : O(n)
Time    : O(n)
"""


def climbingLeaderboard(ranked, player):
    ans = []

    i, j = 0, len(player)-1

    rank = 1
    while i < len(ranked) and j >= 0:
        if player[j] >= ranked[i]:
            ans.insert(0, rank)
            j -= 1
        else:
            i += 1
            if i < len(ranked):
                if ranked[i-1] > ranked[i]:
                    rank += 1

    for x in range(len(ans), len(player)):
        ans.insert(0, rank + 1)

    return ans
