package main

import "golang/model"

/*
Space	: O(n)
Time	: O(n)
*/

func maxAncestorDiff(root *model.TreeNode) int {
	if root == nil {
		return 0
	}

	type Helper struct {
		Node *model.TreeNode
		Max  int
		Min  int
	}

	ans := 0
	stack := []Helper{
		Helper{
			Node: root,
			Max:  -1,
			Min:  100000,
		},
	}

	for len(stack) > 0 {
		temp := []Helper{}
		for _, helper := range stack {
			node := helper.Node
			maxv := Max(helper.Max, node.Val)
			minv := Min(helper.Min, node.Val)

			ans = Max(ans, Abs(maxv-minv))
			if node.Left != nil {
				temp = append(temp, Helper{
					Node: node.Left,
					Max:  maxv,
					Min:  minv,
				})
			}

			if node.Right != nil {
				temp = append(temp, Helper{
					Node: node.Right,
					Max:  maxv,
					Min:  minv,
				})
			}

		}
		stack = temp

	}

	return ans
}
