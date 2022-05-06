package main

"""
Space : O(n)
Time  : O(n)

Method:
Stack 
"""


func removeDuplicates2(s string, k int) string {
	stack := [][]int{}
	ans := ""

	for _, x := range s {
		if len(stack) == 0 {
			stack = append(stack, []int{int(x), 1})
		} else if stack[len(stack)-1][0] == int(x) {
			stack[len(stack)-1][1]++
		} else {
			stack = append(stack, []int{int(x), 1})
		}
		ans += string(x)

		if stack[len(stack)-1][1] == k {
			ans = ans[:len(ans)-k]
			stack = stack[:len(stack)-1]
		}
	}

	return ans
}
