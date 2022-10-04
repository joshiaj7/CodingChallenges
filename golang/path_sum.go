package main

import "golang/model"

type nodeStack struct {
	Node *model.TreeNode
	Path int
}

func hasPathSum(root *model.TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}

	stack := []nodeStack{
		nodeStack{
			Node: root,
			Path: 0,
		},
	}

	for len(stack) > 0 {
		var temp []nodeStack
		for _, ns := range stack {
			node := ns.Node
			path := ns.Path

			if node.Left == nil && node.Right == nil {
				if path+node.Val == targetSum {
					return true
				}
			}
			if node.Left != nil {
				temp = append(temp, nodeStack{Node: node.Left, Path: path + node.Val})
			}
			if node.Right != nil {
				temp = append(temp, nodeStack{Node: node.Right, Path: path + node.Val})
			}
		}
		stack = temp
	}

	return false
}
