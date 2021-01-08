package golang

import (
	"golang/model"
)

/**
Space	: O(n)
Time	: O(n)
*/

func removeNthFromEnd(head *model.ListNode, n int) *model.ListNode {
	var mem []int
	phead := head

	for phead != nil {
		mem = append(mem, phead.Val)
		phead = phead.Next
	}

	ans := &model.ListNode{
		Val: 0,
	}
	pans := ans

	for i := 0; i < len(mem); i++ {
		if i != len(mem)-n {
			pans.Next = &model.ListNode{
				Val: mem[i],
			}
			pans = pans.Next
		}
	}

	return ans.Next
}
