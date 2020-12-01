package golang

/*
	Space	: O(1)
	Time	: O(n)
*/

// TreeNode is a leetcode-format binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func getMaxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	l := getMaxDepth(root.Left) + 1
	r := getMaxDepth(root.Right) + 1

	return max(r, l)
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return getMaxDepth(root)
}
