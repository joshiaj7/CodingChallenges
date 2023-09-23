package main

import "sort"

// space	: O(n)
// time		: O(ns)

func longestStrChain(words []string) int {
	ans := 0
	dp := map[string]int{}
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})

	for _, word := range words {
		dp[word] = 1
		for i := 0; i < len(word); i++ {
			predecessor := word[:i] + word[i+1:]
			if _, ok := dp[predecessor]; ok {
				if dp[word] < dp[predecessor]+1 {
					dp[word] = dp[predecessor] + 1
				}
			}
		}
		ans = Max(ans, dp[word])
	}

	return ans
}
