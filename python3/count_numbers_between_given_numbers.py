"""
hr
Space   : O(n)
Time    : O(n**2)
"""


def countBetween(arr, low, high):
    n = len(low)
    ans = []
    d = {}

    for x in arr:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    for i in range(n):
        count = 0
        for key in d.keys():
            if low[i] <= key and key <= high[i]:
                count += d[key]
        ans.append(count)

    return ans


print(countBetween([4, 8, 7], [2, 4], [8, 4]))
print(countBetween([1, 2, 2, 3, 4, 7], [0, 2], [2, 4]))
