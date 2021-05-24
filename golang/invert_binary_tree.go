package golang

import (
	"golang/model"
)

func invertTree(root *model.TreeNode) *model.TreeNode {
	p := root

	if p != nil {
		p.Left, p.Right = p.Right, p.Left
		invertTree(p.Left)
		invertTree(p.Right)
	}

	return root
}
