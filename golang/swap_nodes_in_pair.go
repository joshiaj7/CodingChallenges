package golang

// Space	: O(1)
// Time		: O(n/ 2)

import (
	"golang/model"
)

 func swapPairs(head *model.ListNode) *model.ListNode {
    ans := &model.ListNode{
		Val:  0,
	}
    point := ans
    
    for head != nil {
        if head.Next != nil {
            point.Next = &model.ListNode {
                Val: head.Next.Val,
            }
            point = point.Next
            point.Next = &model.ListNode {
                Val: head.Val,
            }
            point = point.Next
            head = head.Next.Next
        } else {
            point.Next = &model.ListNode {
                Val: head.Val,
            }
            point = point.Next
            head = head.Next
        }
    }
    
    return ans.Next
}

