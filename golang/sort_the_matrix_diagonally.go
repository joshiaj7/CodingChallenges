package main

import "sort"

/*
Space	: O(mn)
Time	: O(mn* log n)
*/

func diagonalSort(mat [][]int) [][]int {
	m, n := len(mat), len(mat[0])
	d := make(map[int][]int)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if _, ok := d[i-j]; ok {
				d[i-j] = append(d[i-j], mat[i][j])
			} else {
				d[i-j] = []int{mat[i][j]}
			}
		}
	}

	for k, _ := range d {
		sort.Ints(d[k])
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			num := d[i-j][0]
			d[i-j] = d[i-j][1:]
			mat[i][j] = num
		}
	}

	return mat
}
