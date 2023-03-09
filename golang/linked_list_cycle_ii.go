package main

import "golang/model"

func detectCycle(head *model.ListNode) *model.ListNode {
	if head == nil {
		return nil
	}

	h1 := head
	h2 := head
	cyclical := true

	for h1 != nil || h2 != nil {
		h1 = h1.Next
		h2 = h2.Next
		if h2 != nil {
			h2 = h2.Next
		}

		if h1 == nil || h2 == nil {
			cyclical = false
			break
		}

		if h1.Val == h2.Val && h1.Next != nil && h2.Next != nil && h1.Next.Val == h2.Next.Val {
			break
		}
	}

	if !cyclical {
		return nil
	}

	point := head
	for {
		if point.Val == h1.Val && point.Next.Val == h1.Next.Val {
			return point
		}
		point = point.Next
		h1 = h1.Next
	}

}
