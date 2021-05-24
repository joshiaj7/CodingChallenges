package golang

import (
	"golang/model"
)

// Time  : O(n)
// Space : O(1)

func invertTree(root *model.TreeNode) *model.TreeNode {
	p := root

	if p != nil {
		p.Left, p.Right = p.Right, p.Left
		invertTree(p.Left)
		invertTree(p.Right)
	}

	return root
}
