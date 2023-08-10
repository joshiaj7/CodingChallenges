package main

/*
Space	: O(1)
Time	: O(log n)
*/

func searchRotatedArrayII(nums []int, target int) bool {
	n := len(nums)
	left, right := 0, n-1

	for left <= right {
		mid := (left + right) / 2
		if nums[mid] == target {
			return true
		}

		if nums[left] < nums[mid] {
			if nums[left] <= target && target < nums[mid] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else if nums[left] == nums[mid] {
			left++
		} else {
			if nums[mid] < target && target <= nums[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}

	return false
}
