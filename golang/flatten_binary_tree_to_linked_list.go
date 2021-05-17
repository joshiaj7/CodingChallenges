package golang

// Space : O(n)
// Time  : O(n)

import {
	"golang/model"
}

func getTreePreorder(root *model.TreeNode) []int {
	res := []int{}

	if root != nil {
		res = append(res, root.Val)
		if root.Left != nil {
			res = append(res, getTreePreorder(root.Left)...)
		}
		if root.Right != nil {
			res = append(res, getTreePreorder(root.Right)...)
		}
	}

	return res
}

func flatten(root *model.TreeNode) {
	preorder := getTreePreorder(root)

	p := root
	for i, val := range preorder {
		p.Val = val
		p.Left = nil
		if i != len(preorder)-1 {
			p.Right = &model.TreeNode{}
		}

		p = p.Right
	}

}
