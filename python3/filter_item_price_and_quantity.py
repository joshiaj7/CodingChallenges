"""
govtech
Space   : O(n)
Time    : O(n^2)
"""


from collections import defaultdict


def solution(N, itemList, M, query):
    d = defaultdict(list)

    for V, Q in itemList:
        d[Q].append(V)

    for L, R, X, Y in query:
        count = 0
        for q in range(X, Y + 1):
            if q not in d:
                continue

            for V in d[q]:
                if L <= V <= R:
                    count += 1

        print(count)
