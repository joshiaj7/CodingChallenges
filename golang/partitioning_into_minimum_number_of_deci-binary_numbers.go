package main

import "strconv"

// Space   : O(1)
// Time    : O(l)
// Where l = len(n)

func minPartitions(n string) int {
	ans := 0

	for i := 0; i < len(n); i++ {
		num, _ := strconv.Atoi(string(n[i]))
		ans = Max(num, ans)
	}

	return ans
}