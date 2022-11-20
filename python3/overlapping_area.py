"""
govtech
Space   : O(n)
Time    : O(n^2)
"""


def overlap(area1, area2):
    ax1, ay1, ax2, ay2 = area1
    bx1, by1, bx2, by2 = area2

    # getting min coord
    nx1 = max(ax1, bx1)
    ny1 = max(ay1, by1)

    # getting max coord
    nx2 = min(ax2, bx2)
    ny2 = min(ay2, by2)

    a = max(min(ay2, by2) - max(ay1, by1), 0) * max(min(ax2, bx2) - max(ax1, bx1), 0)

    return a, [nx1, ny1, nx2, ny2]


def solution(areas):
    ans = areas[0]
    max_area = 0
    overlap_count = 0
    n = len(areas)

    for i in range(n):
        current = areas[i]
        oc = 0
        area = float("inf")
        for j in range(n):
            if i == j:
                continue

            a, coord = overlap(current, areas[j])
            if a > 0:
                area = min(area, a)
                oc += 1
                current = coord

        if oc >= overlap_count and area > max_area:
            overlap_count = oc
            max_area = area
            ans = current

    return ans
