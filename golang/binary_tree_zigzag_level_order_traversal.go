package main

import "golang/model"

/*
Space	: O(n)
Time	: O(n)
*/

func zigzagLevelOrder(root *model.TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	ans := [][]int{}
	lines := [][]int{}
	stack := []*model.TreeNode{root}
	for len(stack) > 0 {
		line := []int{}
		temp := []*model.TreeNode{}

		for i := 0; i < len(stack); i++ {
			line = append(line, stack[i].Val)
			if stack[i].Left != nil {
				temp = append(temp, stack[i].Left)
			}
			if stack[i].Right != nil {
				temp = append(temp, stack[i].Right)
			}
		}
		stack = temp
		lines = append(lines, line)
	}

	dir := "+"
	for _, arr := range lines {
		if dir == "+" {
			ans = append(ans, arr)
		} else {
			rev := []int{}
			for i := len(arr) - 1; i >= 0; i-- {
				rev = append(rev, arr[i])
			}
			ans = append(ans, rev)
		}

		if dir == "+" {
			dir = "-"
		} else {
			dir = "+"
		}
	}

	return ans
}
