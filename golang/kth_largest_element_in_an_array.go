package main

/*
Space	: O(n)
Time	: O(n)
*/

func findKthLargest(nums []int, k int) int {
	return findKthSmallest(nums, len(nums)+1-k)
}

func findKthSmallest(nums []int, k int) int {
	pos := partitionArray(nums, 0, len(nums)-1)
	if k > pos+1 {
		return findKthSmallest(nums[pos+1:], k-pos-1)
	} else if k < pos+1 {
		return findKthSmallest(nums[:pos], k)
	}
	return nums[pos]
}

func partitionArray(nums []int, l int, r int) int {
	low := l
	for l < r {
		if nums[l] < nums[r] {
			nums[l], nums[low] = nums[low], nums[l]
			low++
		}
		l++
	}
	nums[low], nums[r] = nums[r], nums[low]
	return low
}
