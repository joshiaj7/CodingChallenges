package main

import "golang/model"

/*
Space	: O(1)
Time	: O(1)
*/

func deleteNode(node *model.ListNode) {
	node.Val = node.Next.Val
	node.Next = node.Next.Next
}
