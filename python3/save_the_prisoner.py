"""
Space   : O(1)
Time    : O(1)
"""


def saveThePrisoner(n, m, s):

    left = m % n
    ans = s - 1 + left
    if ans == 0:
        return n
    if ans > n:
        return ans % n
    return ans
