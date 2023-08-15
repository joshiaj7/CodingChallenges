package main

/*
Space	: O(1)
Time	: O(n)
*/

import "golang/model"

func partition(head *model.ListNode, x int) *model.ListNode {
	gte, lt := &model.ListNode{}, &model.ListNode{}
	p1, p2 := gte, lt

	cur := head
	for cur != nil {
		if cur.Val >= x {
			p1.Next = cur
			p1 = cur
			cur = cur.Next
			p1.Next = nil
		} else {
			p2.Next = cur
			p2 = cur
			cur = cur.Next
			p2.Next = nil
		}
	}

	p2.Next = gte.Next
	return lt.Next
}
