package main

// Space : O(row*col)
// Time  : O(row*col)

type NumMatrix struct {
	matrix [][]int
}

func NumMatrixConstructor(matrix [][]int) NumMatrix {
	row, col := len(matrix), len(matrix[0])

	for y := 0; y < row; y++ {
		for x := 1; x < col; x++ {
			matrix[y][x] += matrix[y][x-1]
		}
	}

	return NumMatrix{matrix: matrix}
}

func (obj *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	ans := 0
	for y := row1; y <= row2; y++ {
		if col1-1 >= 0 {
			ans += (obj.matrix[y][col2] - obj.matrix[y][col1-1])
		} else {
			ans += obj.matrix[y][col2]
		}

	}

	return ans
}
