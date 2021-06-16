package main

import (
	"sort"
)

// Space : O(1)
// Time  : O(n log n)

func maximumUnits(boxTypes [][]int, truckSize int) int {
	ans := 0
	sort.SliceStable(boxTypes, func(i, j int) bool {
		return boxTypes[i][1] > boxTypes[j][1]
	})

	for i := 0; i < len(boxTypes); i++ {
		if truckSize-boxTypes[i][0] >= 0 {
			ans += boxTypes[i][0] * boxTypes[i][1]
			truckSize -= boxTypes[i][0]
		} else {
			ans += truckSize * boxTypes[i][1]
			truckSize = 0
		}
		if truckSize == 0 {
			break
		}
	}

	return ans
}
