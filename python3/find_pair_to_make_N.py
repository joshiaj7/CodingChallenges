# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# LINE JAPAN


def arrange_output(p):
    if p[0] < p[1]:
        return [p[0], p[1]]
    return [p[1], p[0]]


def solution(numbers, target):
    """
    Solution description.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    d = {}
    for num in numbers:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    pos = []
    visited = set()
    for i in d.keys():
        j = target - i
        if j in d:
            if target // 2 == i:
                if d[i] > 1:
                    pos.append((i, i))
                    visited.add(i)
                else:
                    continue
            elif i not in visited:
                pos.append((i, j))
                visited.add(i)
                visited.add(j)

    if not pos:
        return []

    if len(pos) == 1:
        return arrange_output(pos[0])

    max_num = float("inf")
    pair = None
    for p in pos:
        if p[0] < max_num or p[1] < max_num:
            max_num = min(p[0], p[1])
            pair = arrange_output(p)

    return pair
