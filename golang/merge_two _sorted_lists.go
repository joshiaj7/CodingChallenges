package main

import (
	"golang/model"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(l1 *model.ListNode, l2 *model.ListNode) *model.ListNode {
	p1, p2 := l1, l2
	ans := &model.ListNode{
		Val: 0,
	}
	pans := ans

	for p1 != nil && p2 != nil {
		if p1.Val < p2.Val {
			pans.Next = &model.ListNode{
				Val: p1.Val,
			}
			p1 = p1.Next
		} else {
			pans.Next = &model.ListNode{
				Val: p2.Val,
			}
			p2 = p2.Next
		}
		pans = pans.Next
	}

	if p1 != nil {
		pans.Next = p1
	}

	if p2 != nil {
		pans.Next = p2
	}

	return ans.Next
}
