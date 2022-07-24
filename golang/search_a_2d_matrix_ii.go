package main

// Space	: O(1)
// Time		: O(m + n)

func searchMatrix(matrix [][]int, target int) bool {
	row := len(matrix)
	col := len(matrix[0])

	y, x := row-1, 0
	for y >= 0 && x < col {
		if matrix[y][x] == target {
			return true
		}

		if matrix[y][x] < target {
			x++
		} else {
			y--
		}
	}

	return false
}
