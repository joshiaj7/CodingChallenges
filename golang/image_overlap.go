package main

/*
Space	: O(n^2)
Time	: O(n^2)
*/

type CoordPair struct {
	First  int
	Second int
}

func largestOverlap(img1 [][]int, img2 [][]int) int {
	var grid1, grid2 [][]int
	var calc []CoordPair
	n := len(img1)

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if img1[i][j] == 1 {
				grid1 = append(grid1, []int{i, j})
			}
			if img2[i][j] == 1 {
				grid2 = append(grid2, []int{i, j})
			}
		}
	}

	for i := 0; i < len(grid1); i++ {
		for j := 0; j < len(grid2); j++ {
			calc = append(calc, CoordPair{grid1[i][0] - grid2[j][0], grid1[i][1] - grid2[j][1]})
		}
	}

	counter := make(map[CoordPair]int)
	m := len(calc)
	if m == 0 {
		return 0
	}

	ans := 0
	for _, item := range calc {
		if _, ok := counter[item]; ok {
			counter[item]++
		} else {
			counter[item] = 1
		}
		ans = Max(ans, counter[item])
	}

	return ans
}
