package model

// TreeNode is a leetcode-format binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// BSTNext is a leetcode-format binary tree with neighbor node
type BSTNext struct {
	Val   int
	Left  *BSTNext
	Right *BSTNext
	Next  *BSTNext
}

// ListNode is a leetcode-format linked list
type ListNode struct {
	Val  int
	Next *ListNode
}

// RandListNode is a leetcode-format linked list with random
type RandListNode struct {
	Val    int
	Next   *RandListNode
	Random *RandListNode
}

// Node is a leetcode-format n-ary tree
type NaryNode struct {
	Val      int
	Children []*NaryNode
}
