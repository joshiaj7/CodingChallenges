package main

import "golang/model"

/*
Space	: O(n)
Time	: O(n)
*/

func findMode(root *model.TreeNode) []int {
	hashmap := map[int]int{}
	ans := []int{}

	stack := []*model.TreeNode{root}
	for len(stack) > 0 {
		var temp []*model.TreeNode

		for _, node := range stack {
			hashmap[node.Val]++
			if node.Left != nil {
				temp = append(temp, node.Left)
			}
			if node.Right != nil {
				temp = append(temp, node.Right)
			}
		}

		stack = temp
	}

	max_count := 0
	for _, v := range hashmap {
		max_count = Max(max_count, v)
	}

	for k, v := range hashmap {
		if v == max_count {
			ans = append(ans, k)
		}
	}

	return ans
}
