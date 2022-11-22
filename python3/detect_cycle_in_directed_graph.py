# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# LINE JAPAN

from collections import defaultdict


def solution(size, edges):
    """
    Solution description.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if not edges:
        return False

    d = defaultdict(set)
    n = len(edges)
    for i in range(0, n, 2):
        d[edges[i]].add(edges[i + 1])

    visited = set()

    # using BFS
    # initial state
    stack = list(d[edges[0]])
    visited.add(edges[0])

    while stack:
        temp = set()
        for i in stack:
            if i in visited:
                return True

            visited.add(i)
            if i not in d:
                continue

            temp.update(d[i])

        stack = list(temp)

    return False
