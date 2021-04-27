package golang

import (
	"golang/model"
)

// Space : O(n)
// Time  : O(n)

func isLLPalindrome(head *model.ListNode) bool {
	mem := []int{}

	for head != nil {
		mem = append(mem, head.Val)
		head = head.Next
	}

	s, e := 0, len(mem)-1
	for s < e {
		if mem[s] != mem[e] {
			return false
		}
		s++
		e--
	}

	return true
}
