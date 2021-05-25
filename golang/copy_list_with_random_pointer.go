package main

import (
	"golang/model"
)

// Space   : O(2n)
// Time    : O(2n)

func copyRandomList(head *model.RandListNode) *model.RandListNode {
	p := head

	for p != nil {
		// save value to next creation
		value := p.Val
		temp := p.Next

		// insert copied current node
		p.Next = &model.RandListNode{
			Val: value,
		}
		p = p.Next

		// point back to original next
		p.Next = temp
		p = p.Next
	}

	// migrate random node
	p = head
	for p != nil {
		if p.Random != nil {
			// save rand
			rand := p.Random

			// insert rand to new rand
			p = p.Next
			p.Random = rand.Next
			p = p.Next
		} else {
			p = p.Next.Next
		}
	}

	// create new node
	ans := &model.RandListNode{
		Val: 0,
	}
	pa := ans
	p = head
	for p != nil {
		// move next
		p = p.Next

		// insert to ans
		pa.Next = p

		// move to next element
		pa = pa.Next
		p = p.Next
	}

	return ans.Next
}
