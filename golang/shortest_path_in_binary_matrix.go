package main

/*
Space	: O(1)
Time	: O(n^2)
*/

func shortestPathBinaryMatrix(grid [][]int) int {
	n := len(grid)

	if grid[0][0] == 1 || grid[n-1][n-1] == 1 {
		return -1
	}

	type coord struct {
		i int
		j int
	}

	xDir := []int{0, 0, 1, -1, 1, 1, -1, -1}
	yDir := []int{1, -1, 0, 0, 1, -1, 1, -1}

	nextCoords := []coord{
		{
			i: 0,
			j: 0,
		},
	}

	grid[0][0] = -1
	for len(nextCoords) > 0 {
		tempCoords := []coord{}

		for _, currCoord := range nextCoords {
			i := currCoord.i
			j := currCoord.j
			for k := 0; k < len(xDir); k++ {
				di := xDir[k]
				dj := yDir[k]

				ni := i + di
				nj := j + dj
				if ni >= 0 && ni < n && nj >= 0 && nj < n {
					if grid[ni][nj] == 0 {
						grid[ni][nj] = grid[i][j] - 1
						tempCoords = append(tempCoords, coord{i: ni, j: nj})
					}
				}
			}
		}

		nextCoords = tempCoords
	}

	if grid[n-1][n-1] < 0 {
		return -grid[n-1][n-1]
	}

	return -1
}
