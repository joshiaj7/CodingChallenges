package golang

// Space   : O(1)
// Time    : O(k)

func maxScore(cardPoints []int, k int) int {
	n := len(cardPoints)

	ans, total := 0, 0
	for j := 0; j < k; j++ {
		ans += cardPoints[j]
	}
	total = ans

	for i := k - 1; i >= 0; i-- {
		total += cardPoints[n-k+i] - cardPoints[i]
		ans = Max(ans, total)
	}

	return ans
}
