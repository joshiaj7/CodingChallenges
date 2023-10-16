package main

/*
Space	: O(nk)
Time	: O(nk)
*/

func getRow(rowIndex int) []int {
	pascal := [][]int{}

	if rowIndex == 0 {
		return []int{1}
	}
	pascal = append(pascal, []int{1})

	if rowIndex == 1 {
		return []int{1, 1}
	}
	pascal = append(pascal, []int{1, 1})

	for i := 2; i <= rowIndex; i++ {
		row := []int{}
		for j := 0; j <= i; j++ {
			if j == 0 || j == i {
				row = append(row, 1)
			} else {
				row = append(row, pascal[len(pascal)-1][j-1]+pascal[len(pascal)-1][j])
			}
		}
		pascal = append(pascal, row)
	}

	return pascal[len(pascal)-1]
}
