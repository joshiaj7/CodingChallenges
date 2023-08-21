package main

import "strings"

/*
Space	: O(2n)
Time	: O(2n)
*/

func repeatedSubstringPattern(s string) bool {
	n := len(s)
	cmp := (s + s)[1 : (n*2)-1]

	return strings.Contains(cmp, s)
}
