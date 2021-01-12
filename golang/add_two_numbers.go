package golang

// Space    : O(1)
// Time     : O(n)

import "golang/model"

 func addTwoNumbers(l1 *model.ListNode, l2 *model.ListNode) *model.ListNode {
    ans := &model.ListNode{
        Val: 0,
    }
    p := ans
    carry := 0

    for l1 != nil || l2 != nil {
        v1, v2 := 0, 0
        
        if l1 != nil {
            v1 = l1.Val
        }
        
        if l2 != nil {
            v2 = l2.Val
        }
        
        v := (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) / 10
        
        p.Next = &model.ListNode{
            Val: v,
        }
        p = p.Next
        
        if l1 != nil {
            l1 = l1.Next
        }
        
        if l2 != nil {
            l2 = l2.Next
        }
    }
    
    if carry != 0 {
        p.Next = &model.ListNode{
            Val: carry,
        }
    }
    
    return ans.Next
}