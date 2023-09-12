package main

/*
Space	: O(n)
Time	: O(n)
*/

func minDeletions(s string) int {
	ans := 0

	charMap := map[rune]int{}
	for _, c := range s {
		charMap[c]++
	}

	memo := map[int]int{}
	for _, val := range charMap {
		for val > 0 {
			if _, ok := memo[val]; ok {
				val--
				ans++
			} else {
				break
			}
		}

		memo[val] = 1
	}

	return ans
}
