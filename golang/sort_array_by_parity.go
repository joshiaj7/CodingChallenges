package main

// Space   : O(1)
// Time    : O(n)

func sortArrayByParity(A []int) []int {
	leng := len(A)
	idx1, idx2 := 0, leng-1
	ans := make([]int, leng)

	for i := 0; i < leng; i++ {
		if A[i]%2 == 0 {
			ans[idx1] = A[i]
			idx1++
		} else {
			ans[idx2] = A[i]
			idx2--
		}
	}

	return ans
}
