package main

import "golang/model"

// Space	: O(n)
// Time		: O(n)

func isSymmetricBFS(root *model.TreeNode) bool {
	stack := []*model.TreeNode{root}

	for len(stack) > 0 {
		temp := []*model.TreeNode{}
		for _, node := range stack {
			if node != nil {
				temp = append(temp, node.Left)
				temp = append(temp, node.Right)
			}
		}

		i, j := 0, len(temp)-1
		for i < j {
			if temp[i] != nil && temp[j] != nil {
				if temp[i].Val != temp[j].Val {
					return false
				}
			} else if temp[i] != nil && temp[j] == nil {
				return false
			} else if temp[i] == nil && temp[j] != nil {
				return false
			}
			i++
			j--
		}

		stack = temp
	}

	return true
}

// Space	: O(1)
// Time		: O(n)

func isSymmetricDFS(root *model.TreeNode) bool {
	return checkIfSymmetric(root.Left, root.Right)
}

func checkIfSymmetric(left *model.TreeNode, right *model.TreeNode) bool {
	if left == nil && right == nil {
		return true
	}

	if left == nil || right == nil {
		return false
	}

	if left.Val != right.Val {
		return false
	}

	return checkIfSymmetric(left.Left, right.Right) && checkIfSymmetric(left.Right, right.Left)
}
