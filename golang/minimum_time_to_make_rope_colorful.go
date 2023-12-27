package main

/*
Space	: O(1)
Time	: O(n)
*/

func minCost(colors string, neededTime []int) int {
	n := len(colors)
	ans := 0

	cur := colors[0]
	maxTime := neededTime[0]
	sumTime := neededTime[0]

	for i := 1; i < n; i++ {
		if colors[i] == cur {
			sumTime += neededTime[i]
			maxTime = Max(maxTime, neededTime[i])
		} else {
			if sumTime > maxTime {
				ans += sumTime - maxTime
			}
			cur = colors[i]
			sumTime = neededTime[i]
			maxTime = neededTime[i]
		}
	}

	if sumTime > maxTime {
		ans += sumTime - maxTime
	}

	return ans
}
