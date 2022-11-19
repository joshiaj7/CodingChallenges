"""
Andrew's monotone chain convex hull algorithm
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        trees = sorted(trees)
        upper, lower = [], []

        # cross_product of 2 vectors
        # counter clockwise: > 0
        # clockwise: < 0
        # collinear: == 0
        def cross(B, A, T):
            Bx, By, Ax, Ay, Tx, Ty = B[0], B[1], A[0], A[1], T[0], T[1]
            return (Ty - By) * (Bx - Ax) - (By - Ay) * (Tx - Bx)

        for T in trees:
            while len(upper) >= 2 and cross(upper[-1], upper[-2], T) < 0:
                upper.pop()
            upper.append(T)

            while len(lower) >= 2 and cross(lower[-1], lower[-2], T) > 0:
                lower.pop()
            lower.append(T)

        return set(tuple(T) for T in (upper + lower))
