package main

/*
Space	: O(m + n)
Time	: O(mn)
*/

func isToeplitzMatrix(matrix [][]int) bool {
	d := make(map[int]int)
	m, n := len(matrix), len(matrix[0])

	for y := 0; y < m; y++ {
		for x := 0; x < n; x++ {
			if _, ok := d[x-y]; ok {
				if d[x-y] != matrix[y][x] {
					return false
				}
			} else {
				d[x-y] = matrix[y][x]
			}
		}
	}

	return true
}
