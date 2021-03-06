package main

import (
	"golang/model"
)

// Space	: O(n)
// Time		: O(n)

func connect(root *model.BSTNext) *model.BSTNext {
	if root == nil {
		return root
	}

	stack := []*model.BSTNext{root}

	for len(stack) > 0 {
		n := len(stack)
		temp := []*model.BSTNext{}

		for i := 0; i < n-1; i++ {
			stack[i].Next = stack[i+1]
		}
		for j := 0; j < n; j++ {
			if stack[j].Left != nil {
				temp = append(temp, stack[j].Left)
			}
			if stack[j].Right != nil {
				temp = append(temp, stack[j].Right)
			}
		}
		stack = temp
	}

	return root
}
