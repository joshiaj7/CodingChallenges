package golang

import (
	"golang/model"
)

func deepestLeavesSum(root *model.TreeNode) int {
	stack := []*model.TreeNode{root}

	for len(stack) > 0 {
		temp := []*model.TreeNode{}
		ans := 0
		for _, node := range stack {
			if node.Left != nil {
				temp = append(temp, node.Left)
			}
			if node.Right != nil {
				temp = append(temp, node.Right)
			}
			ans += node.Val
		}

		if len(temp) == 0 {
			return ans
		}

		stack = temp
	}

	return 0
}
