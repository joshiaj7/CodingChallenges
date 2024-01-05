package main

import "sort"

// Max compare 2 comparables and return the highest value
func Max[T int | float64](a, b T) T {
	if a > b {
		return a
	}
	return b
}

// Min compare 2 int and return the lowest value
func Min(a int, b int) int {
	if a > b {
		return b
	}
	return a
}

// Abs returns positive int from input
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Abs returns positive int from input
func BisectLeft(arr []int, target int) int {
	return sort.Search(len(arr), func(i int) bool {
		return arr[i] >= target
	})
}
