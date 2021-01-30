"""
hr
Space   : O(1)
Time    : O(n)
"""


def collision(speed, pos):
    ans = 0
    n = len(speed)

    for i in range(n):
        if i < pos:
            if speed[i] > speed[pos]:
                ans += 1
        elif i > pos:
            if speed[i] < speed[pos]:
                ans += 1

    return ans


collision([8, 3, 6, 3, 2, 2, 4, 8, 1, 6], 7)
