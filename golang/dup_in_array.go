package golang

// Space   : O(n)
// Time    : O(n)

func findDuplicates(nums []int) []int {
	hashmap := make(map[int]int)
	var ans []int

	for _, val := range nums {
		val = int(val)
		if _, ok := hashmap[val]; ok {
			ans = append(ans, val)
		} else {
			hashmap[val] = 1
		}

	}

	return ans
}
