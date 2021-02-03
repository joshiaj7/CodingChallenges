package golang

import (
	"golang/model"
)

// Space	: O(n)
// Time		: O(1)

func hasCycle(head *model.ListNode) bool {
	if head == nil {
		return false
	}

	p1, p2 := head, head

	for p1 != nil && p2 != nil {
		p1 = p1.Next
		p2 = p2.Next
		if p2 != nil {
			p2 = p2.Next
		}

		if p1 == nil || p2 == nil {
			return false
		}

		if p1.Val == p2.Val {
			if p1.Next.Val == p2.Next.Val {
				break
			}
		}

	}

	return true
}
