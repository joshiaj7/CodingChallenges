package main

/*
Space	: O(n)
Time	: O(n log n)
*/

import "sort"

func bagOfTokensScore(tokens []int, power int) int {
	ans, score := 0, 0
	sort.Ints(tokens)

	for len(tokens) > 0 {
		for len(tokens) > 0 && power >= tokens[0] {
			t := tokens[0]
			tokens = tokens[1:]
			power -= t
			score++
		}

		ans = Max(ans, score)

		if len(tokens) == 0 {
			break
		}

		if score > 0 && power < tokens[0] {
			t := tokens[len(tokens)-1]
			tokens = tokens[:len(tokens)-1]
			power += t
			score -= 1
		} else {
			break
		}

	}

	return ans
}
