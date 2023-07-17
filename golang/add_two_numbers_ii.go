package main

import (
	"golang/model"
	"strconv"
)

/*
Space	: O(n)
Time	: O(n)
*/

func addTwoNumbersII(l1 *model.ListNode, l2 *model.ListNode) *model.ListNode {
	ans := &model.ListNode{}
	l1_str, l2_str := listNodeToStr(l1), listNodeToStr(l2)

	len_l1, len_l2 := len(l1_str), len(l2_str)
	if len_l1 > len_l2 {
		l2_str = addLeadingZero(l2_str, len_l1-len_l2)
	} else {
		l1_str = addLeadingZero(l1_str, len_l2-len_l1)
	}
	n := len(l1_str)

	remainder := 0
	for i := n - 1; i >= 0; i-- {
		i1, _ := strconv.Atoi(string(l1_str[i]))
		i2, _ := strconv.Atoi(string(l2_str[i]))

		total := i1 + i2 + remainder
		digit := total % 10
		if total >= 10 {
			remainder = 1
		} else {
			remainder = 0
		}

		// fmt.Println(digit)
		node := &model.ListNode{Val: digit}
		if i == n-1 {
			node.Next = nil
		} else {
			node.Next = ans
		}
		ans = node
	}

	if remainder == 1 {
		node := &model.ListNode{Val: remainder}
		node.Next = ans
		ans = node
	}

	return ans
}

func listNodeToStr(l *model.ListNode) string {
	s := ""
	p := l

	for p != nil {
		c := strconv.Itoa(p.Val)
		s += c
		p = p.Next
	}

	return s
}

func addLeadingZero(curr string, n int) string {
	for i := 0; i < n; i++ {
		curr = "0" + curr
	}

	return curr
}
