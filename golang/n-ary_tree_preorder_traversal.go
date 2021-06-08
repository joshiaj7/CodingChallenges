package main

import (
	"golang/model"
)

// Space : O(n)
// Time  : O(n)

func getPreorder(root *model.NaryNode) []int {
	res := []int{}

	if root != nil {
		res = append(res, root.Val)
		if len(root.Children) > 0 {
			for _, node := range root.Children {
				res = append(res, getPreorder(node)...)
			}
		}
	}

	return res
}

func preorder(root *model.NaryNode) []int {
	return getPreorder(root)
}
