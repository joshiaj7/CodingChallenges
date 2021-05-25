package main

// Space	: O(m + n)
// Time		: O(m + n)

func merge(nums1 []int, m int, nums2 []int, n int) {
	var temp []int
	i, j := 0, 0

	for i < m && j < n {
		if nums1[i] < nums2[j] {
			temp = append(temp, nums1[i])
			i++
		} else {
			temp = append(temp, nums2[j])
			j++
		}
	}

	if i < m {
		temp = append(temp, nums1[i:m]...)
	}

	if j < n {
		temp = append(temp, nums2[j:n]...)
	}

	for k := 0; k < m+n; k++ {
		nums1[k] = temp[k]
	}
}
