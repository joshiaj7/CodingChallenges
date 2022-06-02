package main

func transpose(matrix [][]int) [][]int {
	row, col := len(matrix), len(matrix[0])
	var ans [][]int

	for x := 0; x < col; x++ {
		line := []int{}
		for y := 0; y < row; y++ {
			line = append(line, matrix[y][x])
		}
		ans = append(ans, line)
	}

	return ans
}
