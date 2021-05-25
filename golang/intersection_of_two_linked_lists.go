package main

import (
	"golang/model"
)

// Space	: O(1)
// Time	: O(n)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *model.ListNode) *model.ListNode {
	la, lb := 0, 0
	pa, pb := headA, headB

	for pa != nil {
		la++
		pa = pa.Next
	}

	for pb != nil {
		lb++
		pb = pb.Next
	}

	pa, pb = headA, headB

	dif := 0
	if la > lb {
		dif = la - lb
		for dif > 0 {
			pa = pa.Next
			dif--
		}
	} else {
		dif = lb - la
		for dif > 0 {
			pb = pb.Next
			dif--
		}
	}

	for pa != nil {
		if pa == pb {
			return pa
		}
		pa = pa.Next
		pb = pb.Next
	}

	return nil

}
