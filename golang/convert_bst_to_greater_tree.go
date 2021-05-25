package main

// Space	: O(n)
// Time 	: O(n)

import (
	"golang/model"
)

func getInorder(root *model.TreeNode) []int {
	res := []int{}

	if root != nil {
		res = append(res, getInorder(root.Left)...)
		res = append(res, root.Val)
		res = append(res, getInorder(root.Right)...)
	}

	return res
}

func insertGreaterTree(root *model.TreeNode, nodes []int) {
	if root != nil && len(nodes) > 0 {
		insertGreaterTree(root.Left, nodes)
		root.Val = nodes[0]
		nodes = append(nodes[:0], nodes[1:]...)
		insertGreaterTree(root.Right, nodes)
	}
}

func convertBST(root *model.TreeNode) *model.TreeNode {
	nodes := getInorder(root)
	for i := len(nodes) - 2; i >= 0; i-- {
		nodes[i] += nodes[i+1]
	}

	point := root
	insertGreaterTree(point, nodes)
	return root
}
