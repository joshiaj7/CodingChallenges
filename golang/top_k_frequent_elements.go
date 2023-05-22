package main

import "sort"

/*
Space	: O(n)
Time	: O(n log n)
*/

func topKFrequent(nums []int, k int) []int {
	countMap := map[int]int{}
	ans := []int{}

	for _, i := range nums {
		if _, ok := countMap[i]; ok {
			countMap[i]++
		} else {
			countMap[i] = 1
		}
	}

	type Item struct {
		key int
		val int
	}

	items := []Item{}
	for k, v := range countMap {
		items = append(items, Item{key: k, val: v})
	}

	sort.Slice(items, func(i, j int) bool {
		return items[i].val > items[j].val
	})

	for i := 0; i < k; i++ {
		ans = append(ans, items[i].key)
	}

	return ans
}
