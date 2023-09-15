package main

import "math"

/*
Space	: O(n)
Time	: O(n^2)
*/

func minCostConnectPoints(points [][]int) int {
	type point struct {
		x int
		y int
	}

	ans := 0
	hashmap := map[point]int{}
	for i, item := range points {
		p := point{x: item[0], y: item[1]}
		if i == 0 {
			hashmap[p] = 0
		} else {
			hashmap[p] = math.MaxInt
		}
	}

	for len(hashmap) > 0 {
		var p point
		curVal := math.MaxInt

		for key, val := range hashmap {
			if val < curVal {
				p = key
				curVal = val
			}
		}
		delete(hashmap, p)
		ans += curVal

		for key, val := range hashmap {
			hashmap[key] = Min(val, Abs(p.x-key.x)+Abs(p.y-key.y))
		}
	}

	return ans
}
