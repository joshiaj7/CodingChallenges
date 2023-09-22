package main

// Space	: O(1)
// Time		: O(n)

func isSubsequence(s string, t string) bool {
	m, n := len(s), len(t)

	i := 0
	for j := 0; j < n; j++ {
		if i == m {
			return true
		}

		if s[i] == t[j] {
			i++
		}
	}

	if i == m {
		return true
	}

	return false
}
