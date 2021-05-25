package main

// Space	: O(n)
// Time		: O(n)

import (
	"golang/model"
)

func addOneRow(root *model.TreeNode, v int, d int) *model.TreeNode {
	if d == 1 {
		ans := &model.TreeNode{
			Val:  v,
			Left: root,
		}
		return ans
	}

	level := 1
	stack := []*model.TreeNode{root}

	for len(stack) > 0 {
		temp := []*model.TreeNode{}
		if level+1 == d {
			for _, node := range stack {
				if node.Left != nil {
					l := node.Left
					node.Left = &model.TreeNode{
						Val:  v,
						Left: l,
					}
				} else {
					node.Left = &model.TreeNode{
						Val: v,
					}
				}

				if node.Right != nil {
					r := node.Right
					node.Right = &model.TreeNode{
						Val:   v,
						Right: r,
					}
				} else {
					node.Right = &model.TreeNode{
						Val: v,
					}
				}
			}
			break
		}
		for _, node := range stack {
			if node.Left != nil {
				temp = append(temp, node.Left)
			}
			if node.Right != nil {
				temp = append(temp, node.Right)
			}
		}

		stack = temp
		level++
	}

	return root
}
