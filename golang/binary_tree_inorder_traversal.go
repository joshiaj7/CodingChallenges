package main

import "golang/model"

func inorderTraversal(root *model.TreeNode) []int {
	var res []int

	if root != nil {
		res = append(res, inorderTraversal(root.Left)...)
		res = append(res, root.Val)
		res = append(res, inorderTraversal(root.Right)...)
	}

	return res
}
