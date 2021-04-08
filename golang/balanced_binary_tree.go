package golang

// Space: O(1)
// Time	: O(n)

import (
	"golang/model"
)

func checkBalanced(root *model.TreeNode, res bool) (int, bool) {
	if root == nil {
		return 0, res
	}

	l, lr := checkBalanced(root.Left, res)
	if !lr {
		return 0, false
	}

	r, rr := checkBalanced(root.Right, res)
	if !rr {
		return 0, false
	}

	if l > r {
		if l-r > 1 {
			res = false
		}
		return l + 1, res
	}

	if r-l > 1 {
		res = false
	}
	return r + 1, res

}

func isBalanced(root *model.TreeNode) bool {
	if root == nil {
		return true
	}

	_, res := checkBalanced(root, true)
	return res
}
