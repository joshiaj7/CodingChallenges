"""
Space   : O(n)
Tine    : O(n)
"""


def viralAdvertising(n):
    if n == 0:
        return 0

    dp = []

    for i in range(n):
        if i == 0:
            dp.append(5 // 2)
        else:
            dp.append((dp[-1] * 3) // 2)

    return sum(dp)
