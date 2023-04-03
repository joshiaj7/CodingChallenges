package main

import "sort"

// Space	: O(1)
// Time		: O(n log n)

func numRescueBoats(people []int, limit int) int {
	ans := 0
	sort.Ints(people)
	n := len(people)
	start, end := 0, n-1

	for start <= end {
		if people[start]+people[end] <= limit {
			start++
		}
		end--
		ans++
	}

	return ans
}
