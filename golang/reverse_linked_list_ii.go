package main

import "golang/model"

func reverseBetween(head *model.ListNode, left int, right int) *model.ListNode {
	if left == right {
		return head
	}

	var temp []int
	p := head
	for p != nil {
		temp = append(temp, p.Val)
		p = p.Next
	}

	for left < right {
		temp[left-1], temp[right-1] = temp[right-1], temp[left-1]
		left++
		right--
	}

	new_head := &model.ListNode{
		Val: temp[0],
	}
	p = new_head
	for i := 1; i < len(temp); i++ {
		p.Next = &model.ListNode{
			Val: temp[i],
		}
		p = p.Next
	}

	return new_head
}