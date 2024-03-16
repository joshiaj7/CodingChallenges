package main

import "sort"

func Findallduplicates(arr []int) []int {
	hashmap := map[int]int{}
	ans := []int{}

	for _, item := range arr {
		hashmap[item]++
	}

	for key, val := range hashmap {
		if val > 1 {
			ans = append(ans, key)
		}
	}
	sort.Ints(ans)

	// code goes here
	return ans
}

func SymmetricTree(strArr []string) string {
	level := 0 // root
	n := len(strArr)

	ans := "true"
	cur := 0
	for {
		window := 1 << level
		if cur+window > n {
			break
		}

		if level == 0 {
			level++
			cur += window
			continue
		}

		arr := strArr[cur : cur+window]
		pref := arr[:window/2]
		suf := arr[window/2:]

		if len(pref) != len(suf) {
			ans = "false"
			break
		}

		for idx := 0; idx < len(pref); idx++ {
			if arr[idx] != arr[len(arr)-1-idx] {
				ans = "false"
				break
			}
		}

		level++
		cur += window
	}

	// code goes here
	return ans

}

func TurnipPrice(arr []int) []int {
	n := len(arr)
	ans := make([]int, n-1)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if arr[i] < arr[j] {
				ans[i] = j - i
				break
			}
		}
	}

	// code goes here
	return ans

}
