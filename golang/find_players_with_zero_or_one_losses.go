package main

import "sort"

/*
Space	: O(n)
Time	: O(n)
*/

func findWinners(matches [][]int) [][]int {
	ans := [][]int{[]int{}, []int{}}
	winnerMap := map[int][]int{}
	loserMap := map[int][]int{}
	participants := map[int]bool{}

	for _, match := range matches {
		winner := match[0]
		loser := match[1]

		winnerMap[winner] = append(winnerMap[winner], loser)
		loserMap[loser] = append(loserMap[loser], winner)
		participants[winner] = true
		participants[loser] = true
	}

	for k, _ := range participants {
		_, isWinner := winnerMap[k]
		losingMatches, isLoser := loserMap[k]

		if isWinner && !isLoser {
			ans[0] = append(ans[0], k)
		} else if isLoser && len(losingMatches) == 1 {
			ans[1] = append(ans[1], k)
		}
	}

	sort.Ints(ans[0])
	sort.Ints(ans[1])

	return ans
}
