"""
Space   : O(n)
Time    : O(n)
"""


def circularArrayRotation(a, k, queries):
    k %= len(a)

    arr = a[-k:] + a[:-k]

    ans = [0] * len(queries)
    for i in range(len(queries)):
        ans[i] = arr[queries[i]]

    return ans
