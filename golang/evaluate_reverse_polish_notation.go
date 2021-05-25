package main

import "strconv"

// Space     : O(n)
// Time      : O(n)

func evalRPN(tokens []string) int {
	stack := []int{}
	n := len(tokens)

	for i := 0; i < n; i++ {
		if tokens[i] == "+" {
			res := stack[len(stack)-2] + stack[len(stack)-1]
			stack = stack[:len(stack)-2]
			stack = append(stack, res)
		} else if tokens[i] == "-" {
			res := stack[len(stack)-2] - stack[len(stack)-1]
			stack = stack[:len(stack)-2]
			stack = append(stack, res)
		} else if tokens[i] == "*" {
			res := stack[len(stack)-2] * stack[len(stack)-1]
			stack = stack[:len(stack)-2]
			stack = append(stack, res)
		} else if tokens[i] == "/" {
			res := stack[len(stack)-2] / stack[len(stack)-1]
			stack = stack[:len(stack)-2]
			stack = append(stack, res)
		} else {
			digit, _ := strconv.Atoi(tokens[i])
			stack = append(stack, digit)
		}
	}

	return stack[0]
}
