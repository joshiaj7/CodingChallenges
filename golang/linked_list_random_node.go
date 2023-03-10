package main

// Space	: O(1)
// Time	: O(n)

import (
	"golang/model"
	"math/rand"
)

type Solution struct {
	LinkedList *model.ListNode
	Length     int
}

func Constructor(head *model.ListNode) Solution {
	p := head
	count := 0
	for p != nil {
		count += 1
		p = p.Next
	}

	return Solution{
		LinkedList: head,
		Length:     count,
	}
}

func (this *Solution) GetRandom() int {
	r := rand.Intn(this.Length)
	p := this.LinkedList
	for r > 0 {
		r--
		p = p.Next
	}
	return p.Val
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(head);
 * param_1 := obj.GetRandom();
 */
