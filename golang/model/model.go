package model

// TreeNode is a leetcode-format binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Node is a leetcode-format binary tree with neighbor node
type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}
