package main

/*
Space	: O(1)
Time	: O(n)
*/

import "golang/model"

func lowestCommonAncestor(root, p, q *model.TreeNode) *model.TreeNode {
	if root == nil || root == p || root == q {
		return root
	}

	var left, right *model.TreeNode
	left = lowestCommonAncestor(root.Left, p, q)
	right = lowestCommonAncestor(root.Right, p, q)

	if left != nil && right != nil {
		return root
	} else if left != nil {
		return left
	} else if right != nil {
		return right
	}
	return nil
}
