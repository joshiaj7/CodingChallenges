package main

// Space   : O(1)
// Time    : O(n)

func maxProfit(prices []int) int {
	start := 10000000
	dp := 0

	for _, v := range prices {
		if v < start {
			start = v
		}
		if dp < v-start {
			dp = v - start
		}
	}

	return dp
}
