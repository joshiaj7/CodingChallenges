from collections import defaultdict

"""
govtech
Space   : O(n)
Time    : O(n^2)
"""


def time_to_sec(s):
    return int(s[:-3]) * 60 + int(s[-2:])


def overlap(x1, y1, x2, y2):
    x1 = time_to_sec(x1)
    y1 = time_to_sec(y1)
    x2 = time_to_sec(x2)
    y2 = time_to_sec(y2)
    return max(min(y2, y1) - max(x2, x1), 0)


def solution(t, a, b):
    a_d, b_d = defaultdict(list), defaultdict(list)

    for ta in a:
        day, start, end = ta.split(" ")
        a_d[int(day)].append((start, end))

    for tb in b:
        day, start, end = tb.split(" ")
        b_d[int(day)].append((start, end))

    ans = []
    for i in range(1, 8):
        if i not in a_d or i not in b_d:
            continue

        a_time = a_d[i]
        a_time.sort(key=lambda x: (x[0], x[1]))
        b_time = b_d[i]
        b_time.sort(key=lambda x: (x[0], x[1]))

        ai, bi = 0, 0
        a_len, b_len = len(a_time), len(b_time)

        while ai < a_len and bi < b_len:
            # a forward
            # if a end time < b start time
            # ai++
            if a_time[ai][1] < b_time[bi][0]:
                ai += 1
                continue

            # b forward
            # if b end time < a start time
            # bi++
            if b_time[bi][1] < a_time[ai][0]:
                bi += 1
                continue

            overlap_time = overlap(
                a_time[ai][0], a_time[ai][1], b_time[bi][0], b_time[bi][1]
            )
            if overlap_time >= int(t):
                start_time = max(a_time[ai][0], b_time[bi][0])
                end_time = min(a_time[ai][1], b_time[bi][1])
                ans.append("{} {} {}".format(i, start_time, end_time))

            if (
                ai + 1 < a_len
                and overlap(
                    a_time[ai + 1][0], a_time[ai + 1][1], b_time[bi][0], b_time[bi][1]
                )
                > 0
            ):
                ai += 1
            elif (
                bi + 1 < b_len
                and overlap(
                    a_time[ai][0], a_time[ai][1], b_time[bi + 1][0], b_time[bi + 1][1]
                )
                > 0
            ):
                bi += 1
            else:
                ai += 1
                bi += 1

    if not ans:
        print("No time to play")
    elif len(ans) == 1:
        print(ans[0])
    else:
        for x in ans:
            print(x)
