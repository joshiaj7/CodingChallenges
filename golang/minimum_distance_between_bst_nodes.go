package main

import (
	"golang/model"
	"sort"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type minDiff struct {
	Node    *model.TreeNode
	PrevVal int
}

func minDiffInBST(root *model.TreeNode) int {
	ans := 10000
	stack := []*model.TreeNode{root}

	vals := []int{}
	for len(stack) > 0 {
		temp := []*model.TreeNode{}
		for _, node := range stack {
			vals = append(vals, node.Val)
			if node.Left != nil {
				temp = append(temp, node.Left)
			}

			if node.Right != nil {
				temp = append(temp, node.Right)
			}
		}
		stack = temp
	}

	sort.Ints(vals)
	for i := 1; i < len(vals); i++ {
		ans = Min(ans, vals[i]-vals[i-1])
	}

	return ans
}
