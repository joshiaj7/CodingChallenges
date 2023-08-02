package main

/*
Space	: O(n)
Time	: O(n!)
*/

func permute(nums []int) [][]int {
	ans := [][]int{}
	path := []int{}

	var getPermutation func()
	getPermutation = func() {
		if len(nums) == 0 {
			ans = append(ans, append([]int{}, path...))
			return
		}

		for i := 0; i < len(nums); i++ {
			popped := nums[i]
			nums = remove(nums, i)
			path = append(path, popped)

			getPermutation()

			nums = insert(nums, i, popped)
			path = path[:len(path)-1]
		}
	}

	getPermutation()
	return ans
}

func remove(nums []int, i int) []int {
	return append(nums[:i], nums[i+1:]...)
}

func insert(nums []int, i int, val int) []int {
	res := []int{}
	res = append(res, nums[:i]...)
	res = append(res, val)
	res = append(res, nums[i:]...)
	return res
}
