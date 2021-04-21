package golang

func minimumTotal(triangle [][]int) int {
	ans := 1000000
	n := len(triangle)

	if n == 1 {
		return triangle[0][0]
	}

	for i := 1; i < n; i++ {
		for j := 0; j < len(triangle[i]); j++ {
			if j == 0 {
				triangle[i][j] += triangle[i-1][j]
			} else if j == len(triangle[i])-1 {
				triangle[i][j] += triangle[i-1][j-1]
			} else {
				triangle[i][j] += Min(triangle[i-1][j-1], triangle[i-1][j])
			}

			if i == n-1 {
				ans = Min(ans, triangle[i][j])
			}
		}
	}

	return ans
}
