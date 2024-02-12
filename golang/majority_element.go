package main

/*
Space	: O(n)
Time	: O(n)
*/

func majorityElement(nums []int) int {
	ans := 0
	hashmap := make(map[int]int)

	for _, x := range nums {
		hashmap[x]++
	}

	count := 0
	for k, v := range hashmap {
		if v > count {
			count = v
			ans = k
		}
	}

	return ans
}
