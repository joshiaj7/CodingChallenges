# Python 3 program to find the size
# of the largest '+' formed by all
# 1's in given binary matrix

# size of binary square matrix
N = 10

# Function to find the size of the
# largest '+' formed by all 1's in
# given binary matrix


def findLargestPlus(mat):
    # left[j][j], right[i][j], top[i][j] and
    # bottom[i][j] store maximum number of
    # consecutive 1's present to the left,
    # right, top and bottom of mat[i][j] including
    # cell(i, j) respectively
    left = [[0 for x in range(N)]
            for y in range(N)]
    right = [[0 for x in range(N)]
             for y in range(N)]
    top = [[0 for x in range(N)]
           for y in range(N)]
    bottom = [[0 for x in range(N)]
              for y in range(N)]

    # initialize above four matrix
    for i in range(N):

        # initialize first row of top
        top[0][i] = mat[0][i]

        # initialize last row of bottom
        bottom[N - 1][i] = mat[N - 1][i]

        # initialize first column of left
        left[i][0] = mat[i][0]

        # initialize last column of right
        right[i][N - 1] = mat[i][N - 1]

    # fill all cells of above four matrix
    for i in range(N):
        for j in range(1, N):

            # calculate left matrix (filled
            # left to right)
            if (mat[i][j] == 1):
                left[i][j] = left[i][j - 1] + 1
            else:
                left[i][j] = 0

            # calculate top matrix
            if (mat[j][i] == 1):
                top[j][i] = top[j - 1][i] + 1
            else:
                top[j][i] = 0

            # calculate new value of j to calculate
            # value of bottom(i, j) and right(i, j)
            j = N - 1 - j

            # calculate bottom matrix
            if (mat[j][i] == 1):
                bottom[j][i] = bottom[j + 1][i] + 1
            else:
                bottom[j][i] = 0

            # calculate right matrix
            if (mat[i][j] == 1):
                right[i][j] = right[i][j + 1] + 1
            else:
                right[i][j] = 0

            # revert back to old j
            j = N - 1 - j

    # n stores length of longest '+'
    # found so far
    n = 0

    # compute longest +
    for i in range(N):
        for j in range(N):

            # find minimum of left(i, j),
            # right(i, j), top(i, j), bottom(i, j)
            l = min(min(top[i][j], bottom[i][j]),
                    min(left[i][j], right[i][j]))

            # largest + would be formed by
            # a cell that has maximum value
            n = max(n, l)

    # 4 directions of length n - 1 and 1
    # for middle cell
    if (n):
        return 4 * (n - 1) + 1

    # matrix contains all 0's
    return 0


# Driver Code
if __name__ == "__main__":

    # Binary Matrix of size N
    mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
           [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
           [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]]

    print(findLargestPlus(mat))

# This code is contributed by ChitraNayal
