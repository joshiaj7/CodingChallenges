package golang

// Space : O(n)
// Time	 : O(n)

import (
	"golang/model"
)

func levelOrder(root *model.TreeNode) [][]int {
	var ans [][]int
	if root == nil {
		return ans
	}

	stack := []*model.TreeNode{root}

	for len(stack) > 0 {
		temp := []*model.TreeNode{}
		level_val := []int{}
		for i := 0; i < len(stack); i++ {
			level_val = append(level_val, stack[i].Val)
			if stack[i].Left != nil {
				temp = append(temp, stack[i].Left)
			}
			if stack[i].Right != nil {
				temp = append(temp, stack[i].Right)
			}
		}

		ans = append(ans, level_val)

		if len(temp) > 0 {
			stack = temp
		} else {
			break
		}
	}

	return ans
}
