package main

import (
	"golang/model"
)

// Space	: O(n)
// Time		: O(n)

func swapNodes(head *model.ListNode, k int) *model.ListNode {
	temp := []int{}
	p := head

	for p != nil {
		temp = append(temp, p.Val)
		p = p.Next
	}

	temp[k-1], temp[len(temp)-k] = temp[len(temp)-k], temp[k-1]

	p = head
	i := 0
	for i < len(temp) {
		p.Val = temp[i]
		i++
		p = p.Next
	}

	return head
}
