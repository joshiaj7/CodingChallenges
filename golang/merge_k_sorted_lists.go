package main

// Space 	: O(nk)
// Time 	: O(nk)

import (
	"golang/model"
	"sort"
)

func mergeKLists(lists []*model.ListNode) *model.ListNode {
	temp := []int{}
	ans := &model.ListNode{Val: 0, Next: nil}
	k := len(lists)
	p := &model.ListNode{}

	for i := 0; i < k; i++ {
		p = lists[i]
		for p != nil {
			temp = append(temp, p.Val)
			p = p.Next
		}
	}

	sort.Ints(temp)
	p = ans
	for _, val := range temp {
		p.Next = &model.ListNode{Val: val, Next: nil}
		p = p.Next
	}

	return ans.Next
}
