package main

import (
	"golang/model"
)

// Space : O(n)
// Time  : O(n)

func naryPostorder(root *model.NaryNode) []int {
	res := []int{}

	if root != nil {
		if len(root.Children) > 0 {
			for _, node := range root.Children {
				res = append(res, naryPostorder(node)...)
			}
		}
		res = append(res, root.Val)
	}

	return res
}

