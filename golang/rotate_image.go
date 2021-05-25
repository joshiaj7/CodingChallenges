package main

// Space : O(1)
// Time : O(n^2)

func rotateMatrix(matrix [][]int) {
	n := len(matrix)

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if i < j {
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
			}
		}
	}

	row := 0
	for row < n {
		s, e := 0, n-1
		for s < e {
			matrix[row][s], matrix[row][e] = matrix[row][e], matrix[row][s]
			s++
			e--
		}
		row++
	}
}
