package main

// Space   : O(1)
// Time    : O(1)

func isPowerOfThree(n int) bool {
	return (n > 0) && (1162261467%n == 0)
}
