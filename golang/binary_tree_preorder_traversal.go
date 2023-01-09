package main

import "golang/model"

/*
Space	: O(n)
Time	: O(n)
*/

func preorderTraversal(root *model.TreeNode) []int {
	res := []int{}
	if root != nil {
		res = append(res, root.Val)
		res = append(res, preorderTraversal(root.Left)...)
		res = append(res, preorderTraversal(root.Right)...)
	}

	return res
}
