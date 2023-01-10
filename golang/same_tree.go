package main

import "golang/model"

/*
Space	: O(n)
Time	: O(n)
*/

func isSameTree(p *model.TreeNode, q *model.TreeNode) bool {
	ap := []*model.TreeNode{p}
	aq := []*model.TreeNode{q}

	for len(ap) > 0 && len(aq) > 0 {
		np := ap[0]
		ap = ap[1:]
		nq := aq[0]
		aq = aq[1:]

		if np == nil && nq == nil {
			continue
		}
		if np != nil && nq != nil {
			if np.Val != nq.Val {
				return false
			}

			ap = append(ap, np.Left)
			ap = append(ap, np.Right)
			aq = append(aq, nq.Left)
			aq = append(aq, nq.Right)
		} else {
			return false
		}
	}

	return true
}
