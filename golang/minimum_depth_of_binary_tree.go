package main

// Space 	: O(n)
// Time	 	: O(n)

import (
	"golang/model"
)

func minDepth(root *model.TreeNode) int {
	level := 1

	if root == nil {
		return 0
	}

	stack := []*model.TreeNode{root}
	for len(stack) > 0 {
		temp := []*model.TreeNode{}

		for _, node := range stack {
			if node.Left == nil && node.Right == nil {
				return level
			}

			if node.Left != nil {
				temp = append(temp, node.Left)
			}

			if node.Right != nil {
				temp = append(temp, node.Right)
			}
		}
		stack = temp
		level++
	}

	return level
}
