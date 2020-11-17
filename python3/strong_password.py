"""
Space   : O(1)
Time    : O(n)
"""

import re


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    ans = 0

    low = re.findall("[a-z]", password)
    if not low:
        ans += 1

    up = re.findall("[A-Z]", password)
    if not up:
        ans += 1

    dig = re.findall("[0-9]", password)
    if not dig:
        ans += 1

    spe = re.findall("[!@#$%^&*()\-+]", password)
    if not spe:
        ans += 1

    if n + ans < 6:
        return 6 - n

    return ans
