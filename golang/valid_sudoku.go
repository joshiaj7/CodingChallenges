package main

/*
	Space	: O(81)
	Time	: O(81)
*/

func isElementValid(truth map[int]map[byte]int, room int, num byte) bool {
	if _, ok := truth[room]; !ok {
		truth[room] = map[byte]int{}
		truth[room][num] = 1
		return true
	}

	if _, ok := truth[room][num]; !ok {
		truth[room][num] = 1
		return true
	}

	return false
}

func isValidSudoku(board [][]byte) bool {
	checkRow := map[int]map[byte]int{}
	checkCol := map[int]map[byte]int{}
	checkSqu := map[int]map[byte]int{}

	M, N := len(board), len(board[0])

	for y := 0; y < M; y++ {
		for x := 0; x < N; x++ {
			isValid := true
			if string(board[y][x]) != "." {
				// check each row
				isValid = isElementValid(checkRow, y, board[y][x])
				if !isValid {
					return false
				}

				// check each column
				isValid = isElementValid(checkCol, x, board[y][x])
				if !isValid {
					return false
				}

				// check each square
				if y < 3 {
					if x < 3 {
						isValid = isElementValid(checkSqu, 1, board[y][x])
					} else if x < 6 {
						isValid = isElementValid(checkSqu, 2, board[y][x])
					} else {
						isValid = isElementValid(checkSqu, 3, board[y][x])
					}
				} else if y < 6 {
					if x < 3 {
						isValid = isElementValid(checkSqu, 4, board[y][x])
					} else if x < 6 {
						isValid = isElementValid(checkSqu, 5, board[y][x])
					} else {
						isValid = isElementValid(checkSqu, 6, board[y][x])
					}
				} else {
					if x < 3 {
						isValid = isElementValid(checkSqu, 7, board[y][x])
					} else if x < 6 {
						isValid = isElementValid(checkSqu, 8, board[y][x])
					} else {
						isValid = isElementValid(checkSqu, 9, board[y][x])
					}
				}
				if !isValid {
					return false
				}
			}
		}
	}

	return true
}
