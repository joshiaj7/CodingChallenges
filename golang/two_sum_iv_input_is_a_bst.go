package main

import "golang/model"

func findTarget(root *model.TreeNode, k int) bool {
	if root == nil {
		return false
	}

	d := make(map[int]int)
	var q []*model.TreeNode
	q = append(q, root)

	for len(q) > 0 {
		node := q[0]
		q = q[1:]

		if _, ok := d[k-node.Val]; ok {
			return true
		}
		d[node.Val] = 1
		if node.Left != nil {
			q = append(q, node.Left)
		}
		if node.Right != nil {
			q = append(q, node.Right)
		}
	}

	return false
}