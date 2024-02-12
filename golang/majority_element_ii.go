package main

// Space : O(n)
// Time  : O(n)

func majorityElementII(nums []int) []int {
	hashmap := map[int]int{}
	ans := []int{}
	n := len(nums)

	for _, x := range nums {
		hashmap[x]++
	}

	for k, v := range hashmap {
		if v > n/3 {
			ans = append(ans, k)
		}
	}

	return ans
}
