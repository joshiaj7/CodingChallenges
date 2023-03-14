package main

// Space 	: O(n)
// Time		: O(n)

import "golang/model"

type sumNumbersHelper struct {
	node *model.TreeNode
	path int
}

func sumNumbers(root *model.TreeNode) int {
	ans := 0
	stack := []sumNumbersHelper{
		sumNumbersHelper{
			node: root,
			path: 0,
		},
	}

	for len(stack) > 0 {
		temp := []sumNumbersHelper{}
		for _, item := range stack {
			if item.node.Left != nil {
				temp = append(temp, sumNumbersHelper{
					node: item.node.Left,
					path: item.path*10 + item.node.Val,
				})
			}
			if item.node.Right != nil {
				temp = append(temp, sumNumbersHelper{
					node: item.node.Right,
					path: item.path*10 + item.node.Val,
				})
			}
			if item.node.Left == nil && item.node.Right == nil {
				ans += item.path*10 + item.node.Val
			}
		}
		stack = temp
	}

	return ans
}
