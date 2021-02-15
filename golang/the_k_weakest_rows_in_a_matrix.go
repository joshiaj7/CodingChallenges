package golang

func kWeakestRows(mat [][]int, k int) []int {
	ans := make([]int, k)
	row, col := len(mat), len(mat[0])
	d := make(map[int]int)
	idx := 0

	for x := 0; x < col; x++ {
		for y := 0; y < row; y++ {
			if _, ok := d[y]; !ok {
				if mat[y][x] == 0 {
					d[y] = idx
					idx++
				}
			}
		}
	}

	if len(d) < k {
		for i := 0; i < row; i++ {
			if _, ok := d[i]; !ok {
				d[i] = idx
				idx++
			}
		}
	}

	for key, val := range d {
		if val < k {
			ans[val] = key
		}
	}

	return ans
}