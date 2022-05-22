package main

/*
Space	: O(1)
Time	: O(n)

Method:
Palindrome stack
*/


func countSubstrings(s string) int {
	ans, n, i := 0, len(s), 0

	for i < n {
		start, end := i, i
		ans++

		for (end+1 < n) && (s[end] == s[end+1]) {
			end++
			ans++
		}

		for (end+1 < n) && (start-1 >= 0) && (s[start-1] == s[end+1]) {
			start--
			end++
			ans++
		}

		i++
	}

	return ans
}
