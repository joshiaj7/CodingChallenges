"""
hr
Space   : O(1)
Time    : O(n**2)
"""


def sorting(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) > (a[j] + a[i]):
                temp = a[j]
                a[j] = a[i]
                a[i] = temp

    return a


def smallestString(substrings):
    return "".join(sorting(substrings))


print(smallestString(['a', 'bd', 'ac', 'cd']))
print(smallestString(['c', 'cc', 'cca', 'cccb']))
print(smallestString(['abc', 'ab', 'bc']))
