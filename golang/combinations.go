package main

/*
Space	: O(k)
Time	: O(k^n)
*/

func combine(n int, k int) [][]int {
	ans := [][]int{}
	path := []int{}
	var getCombination func(int, int)

	getCombination = func(idx, k int) {
		if k == 0 {
			ans = append(ans, append([]int{}, path...))
			return
		}

		for i := idx; i <= n; i++ {
			path = append(path, i)
			getCombination(i+1, k-1)
			path = path[:len(path)-1]
		}
	}

	getCombination(1, k)
	return ans
}
