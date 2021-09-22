package main

// Space	: O(1)
// Time		: O(log n)

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
	left, right := 0, n
	mid := (left + right) / 2

	for left <= right {
		mid = (left + right) / 2
		if !isBadVersion(mid) {
			if left != mid {
				left = mid
			} else {
				left = mid + 1
			}
		} else {
			if !isBadVersion(mid-1) && isBadVersion(mid) {
				break
			} else {
				right = mid
			}
		}
	}
	return mid
}

// mock function
func isBadVersion(n int) bool {
	return n == n
}
