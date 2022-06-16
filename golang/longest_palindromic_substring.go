package main

func longestPalindromeSubstring(s string) string {
	n := len(s)
	cur, longest, st := 0, 0, 0
	i := 0

	for i < n {
		start, end := i, i

		for end+1 < n && s[end] == s[end+1] {
			end++
		}
		i = end + 1

		for end+1 < n && start-1 >= 0 && s[start-1] == s[end+1] {
			end++
			start--
		}

		cur = end - start + 1
		if cur > longest {
			longest = cur
			st = start
		}
	}

	return s[st : st+longest]
}
