package main

import (
	"golang/model"
)

// Space : O(n)
// Time : O(n)

// BSTIterator is the class name of this problem
type BSTIterator struct {
	Nodes []int
}

// GetInorder is to get nodes in BST inorderly
func GetInorder(root *model.TreeNode) []int {
	res := []int{}

	if root != nil {
		res = append(res, GetInorder(root.Left)...)
		res = append(res, root.Val)
		res = append(res, GetInorder(root.Right)...)
	}

	return res
}

// BSTIteratorConstructor is to construct initial BSTIterator
func BSTIteratorConstructor(root *model.TreeNode) BSTIterator {
	return BSTIterator{
		Nodes: GetInorder(root),
	}
}

// Next is to return the first element of Nodes
func (obj *BSTIterator) Next() int {
	val := obj.Nodes[0]
	obj.Nodes = obj.Nodes[1:]
	return val
}

// HasNext is to return if there's still element to return
func (obj *BSTIterator) HasNext() bool {
	return len(obj.Nodes) > 0
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
