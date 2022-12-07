package main

/*
Space	: O(n)
Time	: O(n)
*/

import "golang/model"

func rangeSumBST(root *model.TreeNode, low int, high int) int {
	var ans int
	stack := []*model.TreeNode{root}

	for len(stack) > 0 {
		temp := []*model.TreeNode{}
		for _, node := range stack {
			if node.Val >= low && node.Val <= high {
				ans += node.Val
			}
			if node.Left != nil {
				temp = append(temp, node.Left)
			}
			if node.Right != nil {
				temp = append(temp, node.Right)
			}
		}
		stack = temp
	}

	return ans
}
