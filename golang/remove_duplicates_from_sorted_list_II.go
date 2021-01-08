package golang

import (
	"golang/model"
)

/*
Space	: O(1)
Time	: O(n)
*/

func deleteDuplicates(head *model.ListNode) *model.ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	ph := head
	ans := &model.ListNode{
		Val: 0,
	}
	pans := ans

	for ph != nil {
		if ph.Next == nil {
			pans.Next = ph
			break
		} else if ph.Val == ph.Next.Val {
			rem := ph.Val
			for ph.Val == rem {
				ph = ph.Next
				if ph == nil {
					break
				}
			}
		} else {
			pans.Next = &model.ListNode{
				Val: ph.Val,
			}
			pans = pans.Next
			ph = ph.Next
		}
	}

	return ans.Next
}
