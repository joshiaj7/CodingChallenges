package main

/*
Space	: O(1)
Time	: O(nm)
*/

func minFallingPathSum(matrix [][]int) int {
	var ans int
	n := len(matrix)

	if n == 1 {
		return matrix[0][0]
	}

	for i := 1; i < n; i++ {
		for j := 0; j < n; j++ {
			var minPrev int

			if j == 0 {
				minPrev = Min(matrix[i-1][j], matrix[i-1][j+1])
			} else if j == n-1 {
				minPrev = Min(matrix[i-1][j-1], matrix[i-1][j])
			} else {
				minPrev = Min(matrix[i-1][j-1], matrix[i-1][j])
				minPrev = Min(minPrev, matrix[i-1][j+1])
			}

			matrix[i][j] += minPrev
		}
	}

	for i := n - 1; i < n; i++ {
		for j := 0; j < n; j++ {
			if j == 0 {
				ans = matrix[i][j]
			} else {
				ans = Min(ans, matrix[i][j])
			}
		}
	}

	return ans
}
