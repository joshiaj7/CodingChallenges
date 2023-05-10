package main

/*
Space	: O(n^2)
Time	: O(n^2)
*/

func generateMatrix(n int) [][]int {
	ans := [][]int{}

	// init
	for i := 0; i < n; i++ {
		line := []int{}
		for j := 0; j < n; j++ {
			line = append(line, 0)
		}
		ans = append(ans, line)
	}

	// populate
	count := 1
	i, j := 0, 0
	direction := "r"
	for count <= n*n {
		ans[i][j] = count
		count++

		if direction == "r" {
			if j+1 == n || ans[i][j+1] > 0 {
				direction = "d"
			}
		} else if direction == "d" {
			if i+1 == n || ans[i+1][j] > 0 {
				direction = "l"
			}
		} else if direction == "l" {
			if j-1 == -1 || ans[i][j-1] > 0 {
				direction = "u"
			}
		} else if direction == "u" {
			if i-1 == n || ans[i-1][j] > 0 {
				direction = "r"
			}
		}

		i, j = getNextCoord(i, j, direction)
	}

	return ans
}

func getNextCoord(i int, j int, direction string) (int, int) {
	if direction == "r" {
		return i, j + 1
	} else if direction == "d" {
		return i + 1, j
	} else if direction == "l" {
		return i, j - 1
	}
	return i - 1, j
}
