package main

import "golang/model"

/*
Space	: O(n)
Time	: O(n)
*/

func preorderDifInBST(node *model.TreeNode) []int {
	res := []int{}
	if node != nil {
		res = append(res, preorderDifInBST(node.Left)...)
		res = append(res, node.Val)
		res = append(res, preorderDifInBST(node.Right)...)
	}
	return res
}

func getMinimumDifference(root *model.TreeNode) int {
	if root == nil {
		return 0
	}

	ans := 100000
	pre := preorderDifInBST(root)

	if len(pre) == 0 {
		return pre[0]
	}

	for i := 1; i < len(pre); i++ {
		ans = Min(ans, pre[i]-pre[i-1])
	}
	return ans
}
