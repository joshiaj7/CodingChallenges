package golang

// Space   : O(n)
// Time    : O(n)

func distributeCandies(candies int, numPeople int) []int {
	ans := make([]int, numPeople)
	counter := 1
	idx := 0

	for candies > 0 {
		if candies-counter < 0 {
			ans[idx] += candies
			break
		} else {
			ans[idx] += counter
		}
		candies -= counter
		counter++
		if idx == len(ans)-1 {
			idx = 0
		} else {
			idx++
		}
	}

	return ans
}
