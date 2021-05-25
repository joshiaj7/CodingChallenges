package main

// Space   : O(1)
// Time    : O(1)

func isPowerOfFour(num int) bool {
	return num > 0 && (num&(num-1)) == 0 && (num-1)%3 == 0
}
