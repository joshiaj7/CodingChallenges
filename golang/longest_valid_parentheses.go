package main

/*
Space	: O(1)
Time	: O(n)

Method:
two pointer iteration
*/


func longestValidParentheses(s string) int {
	ans, n := 0, len(s)

	// forward
	count, start := 0, 0
	for i := 0; i < n; i++ {
		if string(s[i]) == "(" {
			count++
		} else {
			count--
		}

		if count < 0 {
			count = 0
			start = i + 1
		} else if count == 0 {
			ans = Max(ans, i-start+1)
		}
	}

	// backward
	count, end := 0, n-1
	for i := n - 1; i > -1; i-- {
		if string(s[i]) == "(" {
			count--
		} else {
			count++
		}

		if count < 0 {
			count = 0
			end = i - 1
		} else if count == 0 {
			ans = Max(ans, end-i+1)
		}
	}

	return ans
}
