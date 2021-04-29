package golang

// Space : O(1)
// Time  : O(n*m)

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	row := len(obstacleGrid)
	col := len(obstacleGrid[0])

	if obstacleGrid[0][0] == 1 || obstacleGrid[row-1][col-1] == 1 {
		return 0
	}

	obstacleGrid[0][0] = -1

	for y := 0; y < row; y++ {
		for x := 0; x < col; x++ {
			if obstacleGrid[y][x] != 1 {
				if 0 < y && y < row && obstacleGrid[y-1][x] < 0 {
					obstacleGrid[y][x] += obstacleGrid[y-1][x]
				}
				if 0 < x && x < col && obstacleGrid[y][x-1] < 0 {
					obstacleGrid[y][x] += obstacleGrid[y][x-1]
				}
			}
		}
	}

	return -obstacleGrid[row-1][col-1]
}
