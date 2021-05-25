package main

// Space   : O(n)
// Time    : O(n)

func validateStackSequences(pushed []int, popped []int) bool {
	n := len(pushed)
	var stack []int
	i, j := 0, 0

	for i < n || len(stack) > 0 {
		if len(stack) > 0 && stack[len(stack)-1] == popped[j] {
			stack = stack[:len(stack)-1]
			j++
		} else if i < n {
			stack = append(stack, pushed[i])
			i++
		} else {
			return false
		}
	}
	return true
}
