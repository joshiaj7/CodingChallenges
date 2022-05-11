package main

/*
Space	: O(5)
Time	: O(n)
*/

func countVowelStrings(n int) int {
	dp := []int{1, 1, 1, 1, 1}

	for n > 1 {
		total := sumArray(dp)
		temp := []int{total}

		for i := 0; i < 4; i++ {
			total -= dp[i]
			temp = append(temp, total)
		}
		dp = temp
		n--
	}

	return sumArray(dp)
}

func sumArray(arr []int) int {
	sum := 0
	for _, x := range arr {
		sum += x
	}
	return sum
}
