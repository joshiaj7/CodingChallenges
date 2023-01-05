package main

import "sort"

/*
Space	: O(1)
Time	: O(n log n)
*/

func findMinArrowShots(points [][]int) int {
	ans := 0

	sort.SliceStable(points, func(i, j int) bool {
		return points[i][1] < points[j][1]
	})

	end := -1
	for _, item := range points {
		s, e := item[0], item[1]
		if end == -1 {
			end = e
			ans++
			continue
		}

		if end < s {
			end = e
			ans++
		}
	}

	return ans
}
