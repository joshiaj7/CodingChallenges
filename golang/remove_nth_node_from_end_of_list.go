package main

import (
	"golang/model"
)

/**
Space	: O(1)
Time	: O(n)
*/

func removeNthFromEnd(head *model.ListNode, n int) *model.ListNode {
	p := head
	l := 0

	for p != nil {
		l++
		p = p.Next
	}

	if n == l {
		return head.Next
	}

	p = head
	stop := l - n
	for stop-1 > 0 {
		stop--
		p = p.Next
	}

	if p.Next.Next == nil {
		p.Next = nil
	} else {
		p.Next = p.Next.Next
	}

	return head
}
