package main

/*
Space	: O(1)
Time	: O(nm)
*/

func numIslands(grid [][]byte) int {
	ans := 0
	m := len(grid)
	n := len(grid[0])
	diri := []int{0, 0, 1, -1}
	dirj := []int{1, -1, 0, 0}

	var crawl func(i, j int)
	crawl = func(i, j int) {
		if string(grid[i][j]) != "1" {
			return
		}

		grid[i][j] = []byte("2")[0]
		for k := 0; k < 4; k++ {
			di := i + diri[k]
			dj := j + dirj[k]

			if (di >= 0 && di < m) && (dj >= 0 && dj < n) {
				crawl(di, dj)
			}
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if string(grid[i][j]) == "1" {
				crawl(i, j)
				ans += 1
			}
		}
	}

	return ans
}
