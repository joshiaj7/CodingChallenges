package main

import (
	"fmt"
	"golang/model"
)

// Space : O(n)
// Time  : O(n)

type NodePathPair struct {
	N *model.TreeNode
	P string
}

func binaryTreePaths(root *model.TreeNode) []string {
	var ans []string
	if root == nil {
		return ans
	}

	var stack = []NodePathPair{
		{root, fmt.Sprintf("%d", root.Val)},
	}

	for len(stack) > 0 {
		var temp []NodePathPair
		for _, pair := range stack {
			if pair.N.Left != nil {
				temp = append(temp, NodePathPair{pair.N.Left, pair.P + fmt.Sprintf("->%d", pair.N.Left.Val)})
			}
			if pair.N.Right != nil {
				temp = append(temp, NodePathPair{pair.N.Right, pair.P + fmt.Sprintf("->%d", pair.N.Right.Val)})
			}
			if pair.N.Left == nil && pair.N.Right == nil {
				ans = append(ans, pair.P)
			}
		}
		stack = temp
	}

	return ans
}
