package main

// Space   : O(n)
// Time    : O(n)

import "golang/model"

func middleNode(head *model.ListNode) *model.ListNode {
	p1, p2 := head, head
	l := 0

	for p1 != nil {
		l++
		p1 = p1.Next
	}

	l /= 2
	for l > 0 {
		p2 = p2.Next
		l--
	}

	return p2
}
