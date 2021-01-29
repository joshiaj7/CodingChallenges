package golang

import (
	"golang/model"
)

/*
	Space	: O(1)
	Time	: O(n)
*/

func getMaxDepth(root *model.TreeNode) int {
	if root == nil {
		return 0
	}

	l := getMaxDepth(root.Left) + 1
	r := getMaxDepth(root.Right) + 1

	return Max(r, l)
}

func maxDepth(root *model.TreeNode) int {
	if root == nil {
		return 0
	}

	return getMaxDepth(root)
}
